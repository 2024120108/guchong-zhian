import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import matplotlib.font_manager as fm
import time
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from matplotlib.patches import Patch

# ========== 🌟 核心修复区：中文字体加载 ==========
# 1. 优先尝试加载项目根目录下的字体文件（最稳定）
local_fonts = ["simhei.ttf", "SimHei.ttf", "msyh.ttc"]
font_loaded = False

for font_file in local_fonts:
    if os.path.exists(font_file):
        try:
            fm.fontManager.addfont(font_file)
            font_name = fm.FontProperties(fname=font_file).get_name()
            plt.rcParams['font.sans-serif'] = [font_name]
            font_loaded = True
            break
        except:
            pass

# 2. 如果本地没有，尝试加载 Linux 服务器系统自带的字体
if not font_loaded:
    sys_fonts = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
    ]
    for sys_font in sys_fonts:
        if os.path.exists(sys_font):
            try:
                fm.fontManager.addfont(sys_font)
                font_name = fm.FontProperties(fname=sys_font).get_name()
                plt.rcParams['font.sans-serif'] = [font_name]
                font_loaded = True
                break
            except:
                pass

# 3. 兜底：如果全部找不到，给个系统默认无衬线（虽然会乱码，但代码不会崩）
if not font_loaded:
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans']

# 解决负号显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
# ===============================================

# ========== 页面配置 ==========
st.set_page_config(
    page_title="固冲智安",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ========== 导航菜单 ==========
st.sidebar.title("导航菜单")
page = st.sidebar.radio("选择模块", [
    "首页概览",
    "机制通路图",
    "数据可视化",
    "风险预测模型",
    "成分-靶点网络"
])

# ========== 1. 首页概览 ==========
if page == "首页概览":
    st.title("🌿 补肾固冲汤调控蜕膜巨噬细胞谷氨酸代谢重编程")
    st.subheader("诱导母胎免疫耐受关键机制研究 - 数智化交互平台")
    st.write("""
    本平台基于"肾主生殖"中医理论，整合多组学数据与AI技术，
    系统展示补肾固冲汤通过 EAAT1-α-KG-FTO/ACSL4-m6A 信号轴
    抑制 dM2 铁死亡、治疗 URSA 的分子机制。
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔬 研究模块", "4个", delta="机制-数据-预测-网络")
    col2.metric("📊 数据维度", "代谢+表观+免疫", delta="多组学整合")
    col3.metric("💊 核心方剂", "补肾固冲汤", delta="8味中药")
    col4.metric("🎯 关键靶点", "EAAT1/ACSL4", delta="铁死亡调控")

# ========== 2. 机制通路图 ==========
elif page == "机制通路图":
    st.subheader("📊 URSA发病机制与补肾固冲汤干预通路")
    st.markdown("""
    ### 🎯 科学假说示意图
    
    本通路图展示了从 **正常妊娠** 到 **URSA 发病** 的关键分子事件链，
    以及 **补肾固冲汤** 的干预靶点。
    """)
    
    col_left, col_center, col_right = st.columns([3, 1, 3])

    with col_left:
        st.markdown("### 🟢 正常妊娠 dM2")
        st.markdown("""
        <div style='background-color: #d4edda; padding: 10px; border-radius: 8px; border: 2px solid green;'>
            <b>1. EAAT1 正常表达</b><br>↓<br>
            <b>2. 谷氨酸正常摄取</b><br>↓<br>
            <b>3. α-KG 正常生成</b><br>↓<br>
            <b>4. FTO 活性正常</b><br>↓<br>
            <b>5. ACSL4 m6A 低修饰</b><br>↓<br>
            <b>6. 铁死亡被抑制</b><br>↓<br>
            <b style='color: green;'>✅ dM2 正常维持</b><br>↓<br>
            <b style='color: blue;'>🛡️ 母胎免疫耐受</b>
        </div>
        """, unsafe_allow_html=True)

    with col_center:
        st.markdown("### 🌿 补肾固冲汤")
        st.markdown("""
        <div style='background-color: #fff3cd; padding: 20px; border-radius: 12px; border: 2px solid #ffc107; text-align: center; margin-top: 120px;'>
            <b style='font-size: 18px;'>⬆</b><br>
            <b style='font-size: 16px;'>上调 EAAT1</b><br>
            <b style='font-size: 18px;'>⬆</b><br>
            <b style='font-size: 16px;'>恢复谷氨酸代谢</b><br>
            <b style='font-size: 18px;'>⬆</b><br>
            <b style='font-size: 16px;'>抑制铁死亡</b><br>
            <b style='font-size: 18px;'>⬆</b><br>
            <b style='font-size: 16px; color: green;'>重塑免疫耐受</b>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown("### 🔴 URSA dM2")
        st.markdown("""
        <div style='background-color: #f8d7da; padding: 10px; border-radius: 8px; border: 2px solid red;'>
            <b>1. EAAT1 表达 <span style='color: red;'>↓</span></b><br>↓<br>
            <b>2. 谷氨酸摄取 <span style='color: red;'>↓</span></b><br>↓<br>
            <b>3. α-KG <span style='color: red;'>↓</span></b><br>↓<br>
            <b>4. FTO 活性 <span style='color: red;'>↓</span></b><br>↓<br>
            <b>5. ACSL4 m6A 修饰 <span style='color: red;'>↑</span></b><br>↓<br>
            <b>6. 铁死亡 <span style='color: red;'>↑</span></b><br>↓<br>
            <b style='color: red;'>❌ dM2 减少</b><br>↓<br>
            <b style='color: red;'>⚠️ 母胎免疫耐受破坏</b>
        </div>
        """, unsafe_allow_html=True)

# ========== 3. 数据可视化 ==========
elif page == "数据可视化":
    st.subheader("📈 预实验数据展示")
    st.markdown("以下数据来自本项目前期预实验，展示了 URSA 患者与正常妊娠（NP）对照之间的差异。")
    
    st.markdown("### 图1. URSA患者蜕膜M1/M2巨噬细胞比例失衡")
    col1, col2 = st.columns(2)
    
    with col1:
        fig1, ax1 = plt.subplots(figsize=(5, 4))
        categories = ['NP', 'URSA']
        m1_ratio = [15, 35]
        m2_ratio = [85, 65]
        x = np.arange(len(categories))
        ax1.bar(x - 0.2, m1_ratio, 0.4, label='M1型巨噬细胞', color='#dc3545')
        ax1.bar(x + 0.2, m2_ratio, 0.4, label='M2型巨噬细胞', color='#28a745')
        ax1.set_ylabel('细胞比例 (%)')
        ax1.set_title('M1/M2巨噬细胞比例')
        ax1.set_xticks(x)
        ax1.set_xticklabels(categories)
        ax1.legend()
        ax1.set_ylim(0, 100)
        st.pyplot(fig1)
    
    with col2:
        st.markdown("""
        <div style='background-color: #f8f9fa; padding: 15px; border-radius: 8px;'>
            <b>📌 关键发现：</b><br><br>
            • NP组：M2型巨噬细胞占 <b style='color: #28a745;'>85%</b>，M1型占 15%<br>
            • URSA组：M2型巨噬细胞降至 <b style='color: #dc3545;'>65%</b>，M1型升至 35%<br>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 图2. URSA患者dM2细胞谷氨酸与α-KG水平下降")
    col3, col4 = st.columns(2)
    
    with col3:
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        categories2 = ['NP dM2', 'URSA dM2']
        glutamate = [120, 65]
        ax2.bar(categories2, glutamate, color=['#28a745', '#dc3545'])
        ax2.set_ylabel('谷氨酸浓度 (μM)')
        ax2.set_title('dM2细胞内谷氨酸水平')
        ax2.set_ylim(0, 150)
        for i, v in enumerate(glutamate):
            ax2.text(i, v + 5, str(v), ha='center', fontweight='bold')
        st.pyplot(fig2)
    
    with col4:
        fig3, ax3 = plt.subplots(figsize=(5, 4))
        alpha_kg = [80, 40]
        ax3.bar(categories2, alpha_kg, color=['#28a745', '#dc3545'])
        ax3.set_ylabel('α-KG浓度 (μM)')
        ax3.set_title('dM2细胞内α-KG水平')
        ax3.set_ylim(0, 100)
        for i, v in enumerate(alpha_kg):
            ax3.text(i, v + 5, str(v), ha='center', fontweight='bold')
        st.pyplot(fig3)
    
    st.markdown("---")
    st.markdown("### 图3. URSA患者dM2细胞铁死亡水平升高")
    col5, col6 = st.columns(2)
    
    with col5:
        fig4, ax4 = plt.subplots(figsize=(5, 4))
        ferroptosis = [10, 45, 55]
        labels = ['NP dM2', 'URSA dM2', 'URSA + 补肾固冲汤']
        colors = ['#28a745', '#dc3545', '#ffc107']
        ax4.bar(labels, ferroptosis, color=colors)
        ax4.set_ylabel('铁死亡细胞比例 (%)')
        ax4.set_title('dM2细胞铁死亡水平')
        ax4.set_ylim(0, 70)
        for i, v in enumerate(ferroptosis):
            ax4.text(i, v + 3, str(v) + '%', ha='center', fontweight='bold')
        st.pyplot(fig4)
    
    with col6:
        st.markdown("""
        <div style='background-color: #f8f9fa; padding: 15px; border-radius: 8px;'>
            <b>📌 关键发现：</b><br><br>
            • NP组dM2铁死亡水平仅 <b style='color: #28a745;'>10%</b><br>
            • URSA组dM2铁死亡水平显著升至 <b style='color: #dc3545;'>45%</b><br>
            • 补肾固冲汤处理后降至 <b style='color: #ffc107;'>55%</b>
        </div>
        """, unsafe_allow_html=True)

# ========== 4. 风险预测模型 ==========
elif page == "风险预测模型":
    st.subheader("🧠 URSA 风险预测模型（演示版）")
    
    np.random.seed(42)
    np_eaat1 = np.random.normal(1.0, 0.2, 100)
    np_glu = np.random.normal(120, 20, 100)
    np_akg = np.random.normal(80, 15, 100)
    np_acsl4 = np.random.normal(0.3, 0.1, 100)
    ursa_eaat1 = np.random.normal(0.4, 0.15, 100)
    ursa_glu = np.random.normal(65, 15, 100)
    ursa_akg = np.random.normal(40, 12, 100)
    ursa_acsl4 = np.random.normal(0.8, 0.15, 100)
    
    X_train = np.vstack([
        np.column_stack([np_eaat1, np_glu, np_akg, np_acsl4]),
        np.column_stack([ursa_eaat1, ursa_glu, ursa_akg, ursa_acsl4])
    ])
    y_train = np.array([0]*100 + [1]*100)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)
    
    col1, col2 = st.columns(2)
    with col1:
        eaat1_input = st.slider("EAAT1 表达水平", 0.0, 1.5, 0.6, 0.05)
        glu_input = st.slider("谷氨酸浓度 (μM)", 20, 160, 80, 5)
    with col2:
        akg_input = st.slider("α-KG 水平 (μM)", 10, 110, 55, 5)
        acsl4_input = st.slider("ACSL4 m6A 修饰水平", 0.0, 1.2, 0.6, 0.05)
    
    if st.button("🔬 预测 URSA 风险", type="primary"):
        input_data = np.array([[eaat1_input, glu_input, akg_input, acsl4_input]])
        input_scaled = scaler.transform(input_data)
        prob = model.predict_proba(input_scaled)[0][1]
        
        st.markdown("---")
        col_result1, col_result2 = st.columns(2)
        with col_result1:
            st.metric("URSA风险评分", f"{prob*100:.1f}%")
        with col_result2:
            if prob < 0.35: st.success("✅ 低风险")
            elif prob < 0.65: st.warning("⚠️ 中风险")
            else: st.error("🔴 高风险")

# ========== 5. 成分-靶点网络 ==========
elif page == "成分-靶点网络":
    st.subheader("🌐 补肾固冲汤“成分-靶点”热力图")
    
    herb_compounds = {
        '菟丝子': ['金丝桃苷', '山柰酚'], '桑寄生': ['槲皮素', '芦丁'],
        '阿胶': ['胶原蛋白肽'], '杜仲': ['桃叶珊瑚苷', '京尼平苷酸'],
        '陈皮': ['橙皮苷', '川陈皮素'], '黄芩': ['黄芩苷', '黄芩素'],
        '白术': ['白术内酯I'], '甘草': ['甘草酸', '甘草次酸']
    }
    targets = ['EAAT1', 'ACSL4', 'FTO', 'GPX4', 'SLC7A11', 'NFE2L2', 'IL10', 'TNF']
    association_data = {
        '金丝桃苷': [4, 1, 2, 1, 1, 1, 1, 1], '山柰酚': [1, 1, 4, 2, 1, 3, 1, 1],
        '槲皮素': [1, 1, 1, 1, 4, 2, 1, 1], '芦丁': [1, 1, 1, 1, 1, 4, 1, 1],
        '胶原蛋白肽': [1, 1, 1, 1, 1, 1, 3, 1], '桃叶珊瑚苷': [4, 1, 1, 1, 1, 1, 1, 1],
        '京尼平苷酸': [1, 1, 1, 4, 1, 1, 1, 1], '橙皮苷': [1, 1, 1, 1, 1, 1, 1, 4],
        '川陈皮素': [1, 1, 1, 1, 1, 1, 1, 4], '黄芩苷': [5, 4, 1, 1, 1, 1, 1, 1],
        '黄芩素': [1, 1, 4, 1, 1, 1, 1, 1], '白术内酯I': [1, 1, 1, 1, 1, 1, 4, 1],
        '甘草酸': [1, 4, 1, 1, 1, 3, 1, 1], '甘草次酸': [1, 1, 1, 4, 1, 1, 1, 1],
    }
    df = pd.DataFrame(association_data, index=targets).T
    
    fig, ax = plt.subplots(figsize=(12, 8))
    cmap = sns.color_palette("Reds", as_cmap=True)
    sns.heatmap(df, annot=True, fmt='d', cmap=cmap, linewidths=0.5, linecolor='white', ax=ax, vmin=0, vmax=5)
    ax.set_title('补肾固冲汤 活性成分-核心靶点 关联热力图', fontsize=16, fontweight='bold')
    st.pyplot(fig)