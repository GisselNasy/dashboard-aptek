import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Kemiskinan Multidimensi Jawa Timur", layout="wide", initial_sidebar_state="expanded")

# ===============================
# CUSTOM CSS
# ===============================
st.markdown("""
<style>
    /* Main background */
    .main {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    /* Card styling */
    .metric-card {
        background: linear-gradient(135deg, #1d5175 0%, #6bb9d4 100%);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
        color: white;
        text-align: center;
        margin: 10px 0;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.25);
    }
    
    .metric-value {
        font-size: 2.8em;
        font-weight: bold;
        margin: 10px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .metric-label {
        font-size: 1.1em;
        opacity: 0.95;
        font-weight: 500;
    }
    
    /* Header styling */
    h1 {
        color: #1d5175 !important;
        font-weight: 700;
        text-shadow: none;
    }
    
    h2 {
        color: #1d5175 !important;
        font-weight: 600;
    }
    
    h3 {
        color: #1d5175 !important;
        font-weight: 600;
    }
    
    /* Info box */
    .info-box {
        background: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #7eeb55;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin: 15px 0;
    }
    
    .info-box h3, .info-box h4, .info-box p, .info-box li, .info-box strong {
        color: #1d5175 !important;
    }
    
    /* Ensure all text elements have proper color */
    p, span, div {
        color: #1d5175;
    }
    
    /* Sidebar styling */
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1d5175 0%, #6bb9d4 100%);
        padding: 2rem 1rem;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] .stMarkdown {
        color: white !important;
    }

    section[data-testid="stSidebar"] .stMultiSelect label {
        color: white !important;
        font-weight: 500;
        font-size: 1.1em;
    }
            
    /* Multiselect pill/tag menjadi warna hijau */
    .stMultiSelect div[data-baseweb="tag"] {
        background-color: #7efc5a !important; /* hijau muda terang */
        color: #06381f !important;            /* teks gelap */
        border-radius: 8px !important;
        padding: 3px 6px !important;
    }

    /* warna ikon X */
    .stMultiSelect div[data-baseweb="tag"] svg {
        fill: #06381f !important;
    }

    /* Dropdown box background */
    .stMultiSelect div[role="listbox"] {
        background-color: #e8ffe1 !important; /* hijau sangat muda */
        color: #06381f !important;
    }
    
    /* Tab styling: unselected tab */
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255,255,255,0.06);
        color: white;
        border-radius: 8px 8px 0 0;
        padding: 8px 14px;
        border: none;
        font-weight: 600;
    }

    /* Selected tab: hijau terang */
    .stTabs [aria-selected="true"] {
        background-color: #7efc5a !important;  /* hijau terang */
        color: #06381f !important;              /* teks gelap untuk kontras */
        font-weight: 800;
        box-shadow: 0 6px 20px rgba(126,250,90,0.18);
    }
            
    .stTabs [data-baseweb="tab"] {
        background-color: white;
        color: #1d5175;
        border-radius: 10px 10px 0 0;
        padding: 12px 24px;
        font-weight: 600;
        border: 2px solid #e9ecef;
    }
    
    /* Stats card */
    .stats-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-top: 4px solid #7eeb55;
        margin: 10px 0;
    }
    
    .stats-card h4 {
        color: #1d5175;
        margin-bottom: 10px;
    }
    
    /* Divider */
    hr {
        border: none;
        border-top: 2px solid #e9ecef;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ===============================
# DATASET
# ===============================

pti_data = pd.DataFrame({
    "Kota": ["Madiun", "Batu", "Sidoarjo", "Mojokerto", "Malang", "Surabaya",
             "Blitar", "Pasuruan", "Probolinggo", "Kediri"],
    "PTI": [-0.631, -0.601, -0.461, -0.109, -0.081, -0.044, -0.034, -0.001, 0.000, 0.006]
})

ipm_data = pd.DataFrame({
    "Kota": ["Surabaya", "Malang", "Madiun", "Sidoarjo", "Kediri", "Mojokerto",
             "Blitar", "Batu", "Pasuruan", "Probolinggo"],
    "IPM": [85.65, 85.55, 85.12, 83.35, 82.71, 82.35, 82.03, 80.35, 79.52, 78.50],
    "P1": [0.41, 0.39, 0.38, 0.63, 0.62, 0.76, 0.84, 0.37, 1.03, 0.36],
    "P2": [0.11, 0.05, 0.05, 0.19, 0.21, 0.15, 0.15, 0.06, 0.22, 0.05],
    "MPI": [0.0451, 0.0195, 0.0190, 0.1197, 0.1302, 0.114, 0.126, 0.0222, 0.2266, 0.018]
})

# Statistika Deskriptif Indikator
statistik_indikator = pd.DataFrame({
    "Indikator": [
        "Angka Harapan Hidup", "Asupan Protein Hewani", "Lama Sekolah",
        "Indeks Literasi Masyarakat", "Akses Sumber Air", "Bahan Bakar Memasak",
        "Kecukupan Mobilitas", "Alat Komunikasi", "Fasilitas Toilet Pribadi",
        "Ketersediaan Aset", "Tingkat Partisipasi Angkatan Kerja", "Modal Protektif"
    ],
    "Mean": [73.29, 9.09, 14.6, 80.15, 98.35, 98.05, 20.37, 95.91, 89.8, 21.66, 71.71, 71.39],
    "Maks": [74.38, 11.88, 15.77, 94.22, 100, 99.84, 25.85, 98.65, 95.45, 29.25, 78.99, 85.04],
    "Min": [70.59, 6.11, 13.66, 54.83, 95.66, 92.82, 12.8, 91.83, 84.21, 13.86, 67.58, 50.53],
    "Varians": [1.52, 3.41, 0.47, 152.14, 2.75, 3.96, 19.24, 6.07, 13.71, 20.9, 11.87, 101.94],
    "Skewness": [-1.37, -0.21, 0.24, -1.15, -0.79, -2.32, -0.59, -0.77, 0.05, -0.1, 1.11, -0.91],
    "Kurtosis": [1.43, -0.91, -0.6, 1.04, -0.97, 6.31, -0.91, -1.1, -1.21, -0.13, 1.05, 0.97],
    "Z": [71.74, 10.5, 12, 70, 96.11, 75, 12.3, 88.93, 85.26, 20, 72.56, 75],
    "M": [100, 100, 21, 100, 100, 100, 100, 100, 100, 100, 100, 100]
})

# PTI Statistics for Table
pti_stats = {
    "Statistik": ["Mean", "Median", "Std Dev", "Min", "Max", "Range", "Q1", "Q3", "IQR"],
    "Nilai": [
        pti_data["PTI"].mean(),
        pti_data["PTI"].median(),
        pti_data["PTI"].std(),
        pti_data["PTI"].min(),
        pti_data["PTI"].max(),
        pti_data["PTI"].max() - pti_data["PTI"].min(),
        pti_data["PTI"].quantile(0.25),
        pti_data["PTI"].quantile(0.75),
        pti_data["PTI"].quantile(0.75) - pti_data["PTI"].quantile(0.25)
    ]
}
pti_stats_df = pd.DataFrame(pti_stats)

def get_cluster(pti):
    if pti < -0.4:
        return "Cluster 1 (Kemampuan Tinggi)"
    elif pti < 0:
        return "Cluster 2 (Kemampuan Menengah)"
    else:
        return "Cluster 3 (Kemampuan Rendah)"

pti_data["Cluster"] = pti_data["PTI"].apply(get_cluster)

# Merge data for filtering
full_data = pti_data.merge(ipm_data, on="Kota", how="left")

# Color mapping
COLORS = {
    "Cluster 1 (Kemampuan Tinggi)": "#7eeb55",
    "Cluster 2 (Kemampuan Menengah)": "#f9b61a",
    "Cluster 3 (Kemampuan Rendah)": "#6bb9d4"
}

# ===============================
# SIDEBAR
# ===============================

st.sidebar.markdown("<h2 style='text-align: center; margin-bottom: 2rem; color: white;'>FILTER & KONTROL</h2>", unsafe_allow_html=True)

st.sidebar.markdown("---")

st.sidebar.markdown("""
<div style='
    background: rgba(255,255,255,0.18);
    padding: 15px;
    border-radius: 10px;
    margin-top: 1rem;
    color: white;
'>
    <h3 style='color: white; margin-bottom: 10px;'>Kelompok 15</h3>
    <p style='color: white; line-height: 1.7; font-size: 0.9em;'>
        Shearani Gino &nbsp;&nbsp;– Matematika (5002221035)<br>
        Sarma Elvita Malona &nbsp;&nbsp;– Matematika (5002221031)<br>
        Gissella Nasywa A. &nbsp;&nbsp;– Matematika (5002221109)
    </p>
</div>
""", unsafe_allow_html=True)


# Filter by cluster
st.sidebar.markdown("<h3 style='margin-bottom: 1rem; color: white;'>Filter Cluster</h3>", unsafe_allow_html=True)
selected_clusters = st.sidebar.multiselect(
    "Pilih cluster untuk analisis:",
    options=["Cluster 1 (Kemampuan Tinggi)", "Cluster 2 (Kemampuan Menengah)", "Cluster 3 (Kemampuan Rendah)"],
    default=["Cluster 1 (Kemampuan Tinggi)", "Cluster 2 (Kemampuan Menengah)", "Cluster 3 (Kemampuan Rendah)"],
    key="cluster_filter"
)

st.sidebar.markdown("---")

# Filter by city
st.sidebar.markdown("<h3 style='margin-bottom: 1rem; color: white;'>Filter Kota</h3>", unsafe_allow_html=True)
selected_cities = st.sidebar.multiselect(
    "Pilih kota untuk analisis:",
    options=sorted(pti_data["Kota"].unique().tolist()),
    default=pti_data["Kota"].unique().tolist(),
    key="city_filter"
)

st.sidebar.markdown("---")

# About section
st.sidebar.markdown("""
<div style='background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px; margin-top: 1rem;'>
    <h3 style='color: white; margin-bottom: 10px;'>Tentang Dashboard</h3>
    <p style='color: white; font-size: 0.9em; line-height: 1.6;'>
        Dashboard ini menampilkan analisis kemiskinan multidimensi di 10 kota urban Jawa Timur 
        menggunakan Indeks Bourguignon-Chakravarty.
    </p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# ---------- Data clean: pastikan numeric ----------
# Konversi kolom yang harusnya numeric menjadi numeric (jika berupa string)
numeric_cols = ["PTI","IPM","MPI","P1","P2"]
for c in numeric_cols:
    if c in full_data.columns:
        full_data[c] = pd.to_numeric(full_data[c], errors="coerce")
# rebuild filtered frames
filtered_pti = pti_data[pti_data["Cluster"].isin(selected_clusters) & pti_data["Kota"].isin(selected_cities)]
filtered_full = full_data[full_data["Cluster"].isin(selected_clusters) & full_data["Kota"].isin(selected_cities)]


# ===============================
# HEADER
# ===============================

st.title("Dinamika Kemiskinan Multidimensi Kawasan Urban Jawa Timur")
st.markdown("<h3 style='color: #6bb9d4; font-style: italic;'>Indeks Kemiskinan Multidimensi Bourguignon-Chakravarty</h3>", unsafe_allow_html=True)
st.markdown("---")

# ===============================
# KEY METRICS
# ===============================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card" style="background: linear-gradient(135deg, #7eeb55 0%, #6bb9d4 100%);">
        <div class="metric-label" style="color: white;">Total Kota Terfilter</div>
        <div class="metric-value" style="color: white;">{len(filtered_pti)}</div>
        <div style="font-size: 0.9em; opacity: 0.9; color: white;">dari 10 kota</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    avg_pti = filtered_pti["PTI"].mean() if len(filtered_pti) > 0 else 0
    st.markdown(f"""
    <div class="metric-card" style="background: linear-gradient(135deg, #1d5175 0%, #6bb9d4 100%);">
        <div class="metric-label" style="color: white;">Rata-rata PTI</div>
        <div class="metric-value" style="color: white;">{avg_pti:.3f}</div>
        <div style="font-size: 0.9em; opacity: 0.9; color: white;">Poverty Trap Index</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    avg_ipm = filtered_full["IPM"].mean() if not filtered_full["IPM"].isna().all() else 0
    st.markdown(f"""
    <div class="metric-card" style="background: linear-gradient(135deg, #6bb9d4 0%, #7eeb55 100%);">
        <div class="metric-label" style="color: white;">Rata-rata IPM</div>
        <div class="metric-value" style="color: white;">{avg_ipm:.2f}</div>
        <div style="font-size: 0.9em; opacity: 0.9; color: white;">Indeks Pembangunan Manusia</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    avg_mpi = filtered_full["MPI"].mean() if not filtered_full["MPI"].isna().all() else 0
    st.markdown(f"""
    <div class="metric-card" style="background: linear-gradient(135deg, #f9b61a 0%, #7eeb55 100%);">
        <div class="metric-label" style="color: white;">Rata-rata MPI</div>
        <div class="metric-value" style="color: white;">{avg_mpi:.4f}</div>
        <div style="font-size: 0.9em; opacity: 0.9; color: white;">Multidimensional Poverty Index</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ===============================
# TABS
# ===============================

tab1, tab2, tab3, tab4 = st.tabs(["Analisis PTI", "Indikator Pembangunan", "Peta Spasial", "Rekomendasi"])

with tab1:
    st.header("Analisis Poverty Trap Index (PTI)")
    
    # Check if there's data to display
    if len(filtered_pti) == 0:
        st.warning("⚠️ Tidak ada data yang sesuai dengan filter yang dipilih. Silakan sesuaikan filter di sidebar.")
    else:
        # Peringkat PTI
        st.subheader("Peringkat PTI Kota Urban Jawa Timur")
        
        # Peringkat PTI (horizontal bar)
        pti_sorted = filtered_pti.sort_values("PTI", ascending=True)
        # buat kolom teks eksplisit sebagai string
        pti_sorted = pti_sorted.assign(PTI_text = pti_sorted["PTI"].round(3).astype(str))

        fig_pti = px.bar(
            pti_sorted,
            x="PTI",
            y="Kota",
            orientation="h",
            text="PTI_text",            # gunakan nama kolom string
            color="Cluster",
            color_discrete_map=COLORS,
            title="<b>Peringkat Poverty Transition Index (PTI)</b>",
        )

        fig_pti.update_traces(
            texttemplate='%{text}',     # tampilkan literal text kolom string
            textposition="outside",
            hovertemplate='<b>%{y}</b><br>PTI: %{x:.3f}<extra></extra>')
        fig_pti.update_layout(
            height=520,
            margin=dict(l=120, r=40, t=80, b=60),
            plot_bgcolor='white',
            paper_bgcolor='white',
            xaxis=dict(title="PTI Value", showgrid=True, gridcolor='rgba(0,0,0,0.05)'),
            yaxis=dict(title="", autorange="reversed"),
            legend=dict(title="Cluster", bgcolor='white', bordercolor='#1d5175', borderwidth=1)
        )
        st.plotly_chart(fig_pti, use_container_width=True)

        
        # Tabel 12 Indikator dengan Statistika Deskriptif
        st.subheader("Statistika Deskriptif 12 Indikator Kemiskinan Multidimensi")
        
        st.markdown("""
        <div class="info-box">
            <p style='line-height: 1.6; color: #1d5175;'>
                Tabel berikut menampilkan statistika deskriptif dari 12 indikator yang digunakan dalam 
                mengukur kemiskinan multidimensi, termasuk nilai mean, maksimum, minimum, varians, 
                skewness, kurtosis, serta ambang batas kemiskinan (Z) dan nilai maksimal (M).
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.dataframe(
            statistik_indikator,
            use_container_width=True,
            height=450
        )

with tab2:
    st.header("Indeks Pembangunan Manusia & Kemiskinan")
    
    if len(filtered_full) == 0:
        st.warning("⚠️ Tidak ada data yang sesuai dengan filter yang dipilih. Silakan sesuaikan filter di sidebar.")
    else:
        # IPM and MPI charts
        colA, colB = st.columns(2)
        
        with colA:
            # IPM
            ipm_data_filtered = filtered_full.dropna(subset=['IPM']).sort_values('IPM', ascending=False)
            if len(ipm_data_filtered) > 0:
                ipm_data_filtered = ipm_data_filtered.assign(IPM_text = ipm_data_filtered["IPM"].round(2).astype(str))
                fig_ipm = px.bar(
                    ipm_data_filtered,
                    x="Kota",
                    y="IPM",
                    text="IPM_text",
                    title="<b>Indeks Pembangunan Manusia (IPM)</b>",
                    color_discrete_sequence=["#1d5175"]
                )
                fig_ipm.update_traces(texttemplate='%{text}', 
                                      textposition='outside',
                                      hovertemplate='<b>%{x}</b><br>IPM: %{y:.2f}<extra></extra>'
                )
                fig_ipm.update_layout(
                    height=420,
                    margin=dict(l=40, r=40, t=60, b=120),
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    yaxis=dict(title="IPM", gridcolor='rgba(0,0,0,0.05)'),
                    xaxis=dict(tickangle=-45)
                )
                st.plotly_chart(fig_ipm, use_container_width=True)
            else:
                st.info("Tidak ada data IPM untuk ditampilkan dengan filter saat ini.")


        st.markdown("""
        <div class="info-box">
            <h4 style='color:#1d5175;'>Interpretasi IPM</h4>
            <p style='color:#1d5175;'>
                Tingginya IPM pada kota-kota seperti Surabaya, Malang, dan Madiun 
                didukung oleh komponen <strong>harapan lama sekolah</strong> dan 
                <strong>angka harapan hidup</strong> yang relatif tinggi.
            </p>
        </div>
        """, unsafe_allow_html=True)

        
        with colB:
            mpi_data_filtered = filtered_full.dropna(subset=['MPI']).sort_values('MPI', ascending=False)
            if len(mpi_data_filtered) > 0:
                mpi_data_filtered = mpi_data_filtered.assign(MPI_text = mpi_data_filtered["MPI"].round(2).astype(str))
                fig_mpi = px.bar(
                    mpi_data_filtered,
                    x="Kota",
                    y="MPI",
                    text="MPI_text",
                    title="<b>Indeks Kemiskinan Multidimensi (MPI)</b>",
                    color_discrete_sequence=["#1d5175"]
                )
                fig_mpi.update_traces(texttemplate='%{text}', textposition='outside',
                                      hovertemplate='<b>%{x}</b><br>MPI: %{y:.2f}<extra></extra>')
                fig_mpi.update_layout(
                    height=420,
                    margin=dict(l=40, r=40, t=60, b=120),
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    yaxis=dict(title="MPI", gridcolor='rgba(0,0,0,0.05)'),
                    xaxis=dict(tickangle=-45)
                )
                st.plotly_chart(fig_mpi, use_container_width=True)
            else:
                st.info("Tidak ada data MPI untuk ditampilkan dengan filter saat ini.")


        st.markdown("""
        <div class="info-box">
            <h4 style='color:#1d5175;'>Interpretasi MPI</h4>
            <p style='color:#1d5175;'>
                Kota Pasuruan mencatat <strong>MPI tertinggi (0,226)</strong>, 
                menunjukkan bahwa kota ini menghadapi hambatan multidimensi terbesar.
            </p>
            <p style='color:#1d5175;'>
                Sementara kota dengan <strong>MPI terendah (0,019–0,020)</strong> 
                seperti Kota Surabaya dan Kota Madiun mengalami deprivasi multidimensi 
                yang sangat minimal.
            </p>
        </div>
        """, unsafe_allow_html=True)

            
        # P1 and P2 charts
        colC, colD = st.columns(2)
        
        with colC:
            p1_data_filtered = filtered_full.dropna(subset=['P1']).sort_values('P1', ascending=False)
            if len(p1_data_filtered) > 0:
                p1_data_filtered = p1_data_filtered.assign(P1_text = p1_data_filtered["P1"].round(2).astype(str))
                fig_p1 = px.bar(
                    p1_data_filtered,
                    x="Kota",
                    y="P1",
                    text="P1_text",
                    title="<b>Indeks Kedalaman Kemiskinan (P1)</b>",
                    color_discrete_sequence=["#1d5175"]
                )
                fig_p1.update_traces(texttemplate='%{text}', textposition='outside',
                                     hovertemplate='<b>%{x}</b><br>P1: %{y:.2f}<extra></extra>')
                fig_p1.update_layout(
                    height=420,
                    margin=dict(l=40, r=40, t=60, b=120),
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    yaxis=dict(title="P1", gridcolor='rgba(0,0,0,0.05)'),
                    xaxis=dict(tickangle=-45)
                )
                st.plotly_chart(fig_p1, use_container_width=True)
            else:
                st.info("Tidak ada data P1 untuk ditampilkan dengan filter saat ini.")


        st.markdown("""
        <div class="info-box">
            <h4 style='color:#1d5175;'>Interpretasi P1 (Kedalaman Kemiskinan)</h4>
            <p style='color:#1d5175;'>
                Kota Pasuruan dan Kota Blitar menunjukkan <strong>P1 tertinggi</strong>, 
                yang mengindikasikan bahwa penduduk miskin di kedua kota ini berada 
                dalam kondisi kemiskinan yang lebih dalam dibandingkan kota lainnya.
            </p>
        </div>
        """, unsafe_allow_html=True)

        
        with colD:
            p2_data_filtered = filtered_full.dropna(subset=['P2']).sort_values('P2', ascending=False)
            if len(p2_data_filtered) > 0:
                p2_data_filtered = p2_data_filtered.assign(P2_text = p2_data_filtered["P2"].round(2).astype(str))
                fig_p2 = px.bar(
                    p2_data_filtered,
                    x="Kota",
                    y="P2",
                    text="P2_text",
                    title="<b>Indeks Keparahan Kemiskinan (P2)</b>",
                    color_discrete_sequence=["#1d5175"]
                )
                fig_p2.update_traces(texttemplate='%{text}', textposition='outside',
                                     hovertemplate='<b>%{x}</b><br>P2: %{y:.2f}<extra></extra>')
                fig_p2.update_layout(
                    height=420,
                    margin=dict(l=40, r=40, t=60, b=120),
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    yaxis=dict(title="P2", gridcolor='rgba(0,0,0,0.05)'),
                    xaxis=dict(tickangle=-45)
                )
                st.plotly_chart(fig_p2, use_container_width=True)
            else:
                st.info("Tidak ada data P2 untuk ditampilkan dengan filter saat ini.")


        st.markdown("""
        <div class="info-box">
            <h4 style='color:#1d5175;'>Interpretasi P2 (Keparahan Kemiskinan)</h4>
            <p style='color:#1d5175;'>
                Kota Pasuruan memiliki <strong>P2 tertinggi (0,22)</strong>, 
                menunjukkan distribusi kemiskinan yang lebih parah dan tidak merata.
            </p>
            <p style='color:#1d5175;'>
                Kabupaten Batu, Kota Surabaya, Malang, Madiun, dan Probolinggo 
                memiliki <strong>P2 terendah (0,05–0,11)</strong>, 
                mencerminkan kondisi kemiskinan yang tidak terlalu ekstrem.
            </p>
        </div>
        """, unsafe_allow_html=True)


with tab3:
    
    st.header("Peta Spasial Cluster Kemiskinan")

    # Siapkan dataframe peta (pakai filtered_pti agar bereaksi pada filter)
    map_df = filtered_pti.copy()

    # Koordinat (sudah ada; pastikan konsisten dengan data)
    coords = {
        "Madiun": [-7.63, 111.52], "Batu": [-7.87, 112.53], "Sidoarjo": [-7.45, 112.72],
        "Mojokerto": [-7.47, 112.44], "Malang": [-7.98, 112.63], "Surabaya": [-7.25, 112.75],
        "Blitar": [-8.10, 112.17], "Pasuruan": [-7.65, 112.53], "Probolinggo": [-7.75, 113.22], "Kediri": [-7.81, 112.01]
    }

    # Tambah kolom Lat/Lon
    map_df["Lat"] = map_df["Kota"].map(lambda x: coords.get(x, [None, None])[0])
    map_df["Lon"] = map_df["Kota"].map(lambda x: coords.get(x, [None, None])[1])

    # Hapus baris tanpa koordinat jika ada
    map_df = map_df.dropna(subset=["Lat", "Lon"])

    # Jika tidak ada data setelah filter, tampilkan info
    if map_df.empty:
        st.info("Tidak ada kota yang memenuhi filter untuk ditampilkan pada peta.")
    else:
        # Buat peta scatter_mapbox; warnai berdasarkan Cluster
        fig_map = px.scatter_mapbox(
            map_df,
            lat="Lat",
            lon="Lon",
            hover_name="Kota",
            hover_data={"PTI": ":.3f", "Cluster": True, "Lat": False, "Lon": False},
            color="Cluster",
            color_discrete_map=COLORS,
            size=[35] * len(map_df),
            zoom=7.5,
            mapbox_style="carto-positron",
            title="<b>Peta Cluster Kemampuan Keluar dari Kemiskinan (PTI)</b>",
            height=640
        )

        # Perbaikan tata letak agar sesuai tema
        fig_map.update_layout(
            margin={"r":10,"t":50,"l":10,"b":10},
            legend=dict(title="Cluster", bgcolor='rgba(255,255,255,0.9)', bordercolor='#cccccc', borderwidth=1),
            title_font=dict(size=16, color='white'),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )

        # Atur style pop-up agar teks jelas (pakai warna gelap untuk konten peta terang)
        fig_map.update_traces(marker=dict(opacity=0.9, size=14))

        st.plotly_chart(fig_map, use_container_width=True)

    # Keterangan Cluster
    st.subheader("Keterangan Cluster Kemampuan Keluar dari Kemiskinan")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="info-box" style="border-left-color: #7eeb55;">
            <h4 style="color: #7eeb55;">● Cluster 1 – Kemampuan Tinggi</h4>
            <p style='color: #1d5175;'><strong style='color: #1d5175;'>Kriteria:</strong> PTI < -0.4</p>
            <p style='color: #1d5175;'><strong style='color: #1d5175;'>Anggota:</strong></p>
            <ul>
                <li style='color: #1d5175;'>Kota Madiun</li>
                <li style='color: #1d5175;'>Kota Batu</li>
            </ul>
            <p style="font-size: 0.9em; margin-top: 10px; color: #1d5175;">
                Kota-kota dengan kemampuan tinggi untuk keluar dari kemiskinan, 
                ditandai dengan infrastruktur dan layanan sosial yang baik.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-box" style="border-left-color: #f9b61a;">
            <h4 style="color: #f9b61a;">● Cluster 2 – Kemampuan Menengah</h4>
            <p style='color: #1d5175;'><strong style='color: #1d5175;'>Kriteria:</strong> -0.4 < PTI < 0</p>
            <p style='color: #1d5175;'><strong style='color: #1d5175;'>Anggota:</strong></p>
            <ul>
                <li style='color: #1d5175;'>Sidoarjo</li>
                <li style='color: #1d5175;'>Mojokerto</li>
                <li style='color: #1d5175;'>Malang</li>
                <li style='color: #1d5175;'>Surabaya</li>
                <li style='color: #1d5175;'>Blitar</li>
            </ul>
            <p style="font-size: 0.9em; margin-top: 10px; color: #1d5175;">
                Kota dengan potensi menengah, memerlukan peningkatan 
                pada beberapa aspek untuk naik ke cluster tinggi.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="info-box" style="border-left-color: #6bb9d4;">
            <h4 style="color: #6bb9d4;">● Cluster 3 – Kemampuan Rendah</h4>
            <p style='color: #1d5175;'><strong style='color: #1d5175;'>Kriteria:</strong> PTI ≥ 0</p>
            <p style='color: #1d5175;'><strong style='color: #1d5175;'>Anggota:</strong></p>
            <ul>
                <li style='color: #1d5175;'>Pasuruan</li>
                <li style='color: #1d5175;'>Probolinggo</li>
                <li style='color: #1d5175;'>Kediri</li>
            </ul>
            <p style="font-size: 0.9em; margin-top: 10px; color: #1d5175;">
                Kota yang memerlukan perhatian khusus dan intervensi intensif 
                untuk meningkatkan kemampuan keluar dari kemiskinan.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

with tab4:
    st.header("Rekomendasi Kebijakan")

    st.markdown("""
    <div class="info-box">
        <h3 style='color: #1d5175;'>Rekomendasi Berdasarkan Cluster</h3>
        <p style='line-height: 1.8; color: #1d5175;'>
            Berikut adalah rekomendasi kebijakan yang disesuaikan dengan karakteristik 
            masing-masing cluster kemampuan keluar dari kemiskinan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-box" style="border-left-color: #7eeb55;">
            <h4 style="color: #7eeb55;">🟢 Cluster 1 - Kemampuan Tinggi</h4>
            <p style='color: #1d5175;'><strong style='color: #1d5175;'>Kota:</strong> Madiun, Batu</p>
            <h5 style='color: #1d5175; margin-top: 15px;'>Strategi Utama:</h5>
            <ul style='line-height: 1.8; color: #1d5175;'>
                <li>Mengembangkan pusat inovasi dan ekonomi berbasis pengetahuan.</li>
                <li>Meningkatkan sektor industri kreatif dan jasa bernilai tambah tinggi.</li>
                <li>Menjaga kualitas hidup untuk mempertahankan talenta lokal.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box" style="border-left-color: #6bb9d4;">
            <h4 style="color: #6bb9d4;">🔵 Cluster 3 - Kemampuan Rendah</h4>
            <p style='color: #1d5175;'><strong style='color: #1d5175;'>Kota:</strong> Pasuruan, Probolinggo, Kediri</p>
            <h5 style='color: #1d5175; margin-top: 15px;'>Strategi Utama:</h5>
            <ul style='line-height: 1.8; color: #1d5175;'>
                <li>Penguatan pendidikan vokasi yang relevan dengan industri.</li>
                <li>Pengembangan jaminan sosial yang lebih komprehensif.</li>
                <li>Diversifikasi ekonomi agar tidak bergantung pada satu sektor.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-box" style="border-left-color: #f9b61a;">
            <h4 style="color: #f9b61a;">🟡 Cluster 2 - Kemampuan Menengah</h4>
            <p style='color: #1d5175;'><strong style='color: #1d5175;'>Kota:</strong> Sidoarjo, Mojokerto, Malang, Surabaya, Blitar</p>
            <h5 style='color: #1d5175; margin-top: 15px;'>Strategi Utama:</h5>
            <ul style='line-height: 1.8; color: #1d5175;'>
                <li>Program afirmasi untuk meningkatkan partisipasi angkatan kerja.</li>
                <li>Pelatihan vokasi terintegrasi dengan penempatan kerja.</li>
                <li>Insentif untuk UMKM dan kewirausahaan lokal.</li>
                <li>Perbaikan layanan dasar & infrastruktur.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # General recommendations
    st.markdown("""
    <div class="info-box" style="border-left-color: #1d5175;">
        <h3 style='color: #1d5175;'>Rekomendasi untuk Pemerintah Provinsi Jawa Timur</h3>
        <ol style='line-height: 2; color: #1d5175;'>
            <li><strong style='color: #1d5175;'>Mengembangkan kebijakan pembangunan berbasis kluster kemiskinan.</li>
            <li><strong style='color: #1d5175;'>Memperkuat konektivitas dan sinergi antar kota.</li>
            <li><strong style='color: #1d5175;'>Mendorong pertukaran best practices antara kota kluster tinggi dan kluster lainnya.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #1d5175; padding: 18px;'><p style='font-size: 1.05em;'><strong>Dashboard Kemiskinan Multidimensi Jawa Timur 2025</strong></p><p style='font-size: 0.9em; opacity: 0.85;'>Menggunakan Indeks Bourguignon-Chakravarty</p></div>", unsafe_allow_html=True)


st.markdown("""
<style>

[data-baseweb="tag"] {
    background-color: #86b102 !important;
    color: #06381f !important;
    border-radius: 6px !important;
}

div[role="option"] {
    background-color: #86b102 !important;
    color: #06381f !important;
}

.stMultiSelect [data-baseweb="tag"] {
    background-color: #86b102 !important;
    color: #06381f !important;
}

[data-baseweb="tag"] svg {
    fill: #06381f !important;
}

</style>
""", unsafe_allow_html=True)
