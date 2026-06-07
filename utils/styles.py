def load_css():
    return """
        <style>
        /* ------------------------
        BACKGROUND
        ------------------------ */
        .stApp{
        background:
        linear-gradient(
        120deg,
        #3f1a76 0%,
        #020b25 25%,
        #02133f 70%,
        #2857c5 100%
        );
        color:white;
        }
        /* ------------------------
        HIDE STREAMLIT DEFAULT NAV
        ------------------------ */
        [data-testid="stSidebarNav"]{
        display:none;
        }
        /* ------------------------
        SIDEBAR
        ------------------------ */
        section[data-testid="stSidebar"]{
        background:rgba(15,20,35,0.95);
        backdrop-filter:blur(20px);
        }
        /* ------------------------
        SIDEBAR BOXES
        ------------------------ */
        .sidebar-btn{
        display:flex;
        align-items:center;
        gap:14px;
        padding:16px;
        margin-bottom:14px;
        border-radius:14px;
        background:
        rgba(255,255,255,0.06);
        font-size:19px;
        font-weight:600;
        transition:.3s;
        cursor:pointer;
        }
        .sidebar-btn:hover{
        background:rgba(124,58,237,0.4);
        transform:translateX(5px);
        }
        .sidebar-icon{
        font-size:24px;
        }
        /* ------------------------
        TOP BAR
        ------------------------ */
        .topbar{
        display:flex;
        justify-content:center;
        align-items:center;
        gap:22px;
        margin-top:10px;
        }
        .logo{
        width:74px;
        height:74px;
        border-radius:20px;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:32px;
        background:rgba(255,255,255,0.08);
        }
        .brand{
        font-size:64px;
        font-weight:700;
        }
        .subtitle{
        text-align:center;
        font-size:20px;
        margin-top:12px;
        margin-bottom:35px;
        }
        /* INPUTS */
        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox div{
        background:rgba(255,255,255,0.12)!important;
        border-radius:14px!important;
        color:white!important;
        }
        /* BUTTON */
        .stButton button{
        background:
        linear-gradient(90deg,#7c3aed,#3267ff)!important;
        border:none!important;
        border-radius:18px!important;
        color:white!important;
        height:58px!important;
        font-size:22px!important;
        width:100%!important;
        }
        /* STEPS BOX */
        .steps{
        background:rgba(255,255,255,0.06);
        padding:40px;
        border-radius:28px;
        }
        </style>
        """