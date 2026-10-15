import streamlit as st
import sqlite3

# ==========================================
# 1. إعدادات الصفحة وتصميم منصة الـ Hacking Lab
# ==========================================
st.set_page_config(
    page_title="متجر يونس الضعيف - CTF Security Lab",
    page_icon="🏴‍☠️",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top right, #180505, #09090b 60%, #030014);
        background-attachment: fixed;
        color: #f8fafc;
        font-family: 'Inter', system-ui, sans-serif;
    }
    .lab-header {
        background: rgba(127, 29, 29, 0.3);
        border: 1px solid #dc2626;
        padding: 20px;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 20px;
    }
    .flag-box {
        background: rgba(20, 83, 45, 0.4);
        border: 1px solid #16a34a;
        padding: 15px;
        border-radius: 10px;
        color: #4ade80;
        font-weight: bold;
    }
    .stButton>button {
        border-radius: 8px !important;
        background: #dc2626 !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. إعداد قاعدة بيانات محلية وهمية (تحتوي على ثغرات)
# ==========================================
def init_db():
    conn = sqlite3.connect('vulnerable_app.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            is_admin INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            comment TEXT
        )
    ''')
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (username, password, is_admin) VALUES ('admin', 'SecretAdmin123', 1)")
        cursor.execute("INSERT INTO users (username, password, is_admin) VALUES ('youssef', '123456', 0)")
        conn.commit()
    return conn

conn = init_db()
cursor = conn.cursor()

# ==========================================
# 3. واجهة الموقع المزيف مع أقسام واضحة في الأعلى للجوال
# ==========================================
st.markdown("""
    <div class="lab-header">
        <h2 style="margin:0; color: #f87171;">🏴‍☠️ مختبر الثغرات والتخريب (Vulnerable CTF Lab)</h2>
        <p style="margin:5px 0 0 0; color:#cbd5e1; font-size:13px;">موقع اختباري يحتوي على ثغرات مقصودة لاكتشافها واستغلالها!</p>
    </div>
""", unsafe_allow_html=True)

# استخدام أزرار تبويب في الأعلى لسهولة التصفح من الجوال بدون الحاجة للشريط الجانبي
menu = st.radio(
    "🧭 حدد القسم الانتقالي:",
    ["🏠 الرئيسية", "🔐 تسجيل الدخول", "💬 التعليقات", "🕵️‍♂️ كشف التحديات"],
    horizontal=True
)

st.divider()

# ------------------------------------------
# الصفحة الأولى: الرئيسية
# ------------------------------------------
if menu == "🏠 الرئيسية":
    st.subheader("مرحباً بك في موقع خدمات يونس التجاري")
    st.write("هذا الموقع مصمم خصيصاً لاختبار مهاراتك الأمنية. تجول في الأقسام وابحث عن الثغرات البرمجية!")
    st.info("💡 **تلميح للمحقق:** جرب تسجيل الدخول بصلاحيات المدير `admin` بدون معرفة كلمة المرور عبر التلاعب بالمدخلات (SQLi).")

# ------------------------------------------
# الصفحة الثانية: تسجيل الدخول (SQL Injection)
# ------------------------------------------
elif menu == "🔐 تسجيل الدخول":
    st.subheader("تسجيل الدخول إلى حسابك")
    
    username_input = st.text_input("اسم المستخدم:")
    password_input = st.text_input("كلمة المرور:", type="password")
    
    if st.button("دخول"):
        query = f"SELECT * FROM users WHERE username = '{username_input}' AND password = '{password_input}'"
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            
            if user:
                st.success(f"🎉 تم تسجيل الدخول بنجاح! مرحباً بك يا {user[1]}")
                if user[3] == 1:
                    st.markdown('<div class="flag-box">🚩 FLAG 1 مكتشف: SQL_INJECTION_MASTER_2026</div>', unsafe_allow_html=True)
            else:
                st.error("❌ اسم المستخدم أو كلمة المرور غير صحيحة.")
        except Exception as e:
            st.error(f"حدث خطأ في قاعدة البيانات: {e}")

# ------------------------------------------
# الصفحة الثالثة: التعليقات (Stored XSS)
# ------------------------------------------
elif menu == "💬 التعليقات":
    st.subheader("آراء المستخدمين والتعليقات")
    
    comment_user = st.text_input("اسمك:", value="زائر")
    new_comment = st.text_area("اكتب تعليقك هنا:")
    
    if st.button("إرسال التعليق"):
        if new_comment:
            cursor.execute("INSERT INTO comments (user, comment) VALUES (?, ?)", (comment_user, new_comment))
            conn.commit()
            st.success("تم إرسال تعليقك!")

    st.divider()
    st.markdown("### التعليقات السابقة:")
    cursor.execute("SELECT user, comment FROM comments")
    rows = cursor.fetchall()
    
    for r in rows:
        st.markdown(f"""
            <div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px; margin-bottom: 8px;">
                <b>{r[0]} قال:</b><br>{r[1]}
            </div>
        """, unsafe_allow_html=True)

    st.info("💡 **تلميح XSS:** جرب كتابة كود جافاسكريبت داخل التعليق مثل: `<script>alert('XSS Found!')</script>`")

# ------------------------------------------
# الصفحة الرابعة: كشف التحديات
# ------------------------------------------
elif menu == "🕵️‍♂️ كشف التحديات":
    st.subheader("🎯 قائمة التحديات المطلوب اكتشافها:")
    st.markdown("""
    1. **التحدي الأول (SQL Injection):** حاول الدخول لصفحة المشرف `admin` بدون كلمة مرور.
    2. **التحدي الثاني (Stored XSS):** اجعل الموقع ينفذ كود تنبيه (`alert`) من خلال التعليقات.
    3. **التحدي الثالث (Information Disclosure):** أين يتم حفظ كلمات المرور؟
    """)
