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
    # جدول المستخدمين (كلمات المرور مكشوفة بدون تشفير!)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            is_admin INTEGER
        )
    ''')
    # جدول التعليقات (يقبل XSS)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            comment TEXT
        )
    ''')
    # إدخال بيانات تجريبية
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (username, password, is_admin) VALUES ('admin', 'SecretAdmin123', 1)")
        cursor.execute("INSERT INTO users (username, password, is_admin) VALUES ('youssef', '123456', 0)")
        conn.commit()
    return conn

conn = init_db()
cursor = conn.cursor()

# ==========================================
# 3. واجهة الموقع المزيف
# ==========================================
st.markdown("""
    <div class="lab-header">
        <h2 style="margin:0; color: #f87171;">🏴‍☠️ مختبر الثغرات والتخريب (Vulnerable CTF Lab)</h2>
        <p style="margin:5px 0 0 0; color:#cbd5e1; font-size:13px;">هذا الموقع يحتوي على ثغرات مقصودة. مهمتك هي اكتشافها واستغلالها!</p>
    </div>
""", unsafe_allow_html=True)

menu = st.sidebar.radio("🧭 التنقل في الموقع:", ["🏠 الصفحة الرئيسية", "🔐 تسجيل الدخول", "💬 قسم التعليقات (Community)", "🕵️‍♂️ لوحة كشف التحديات (Flags)"])

# ------------------------------------------
# الصفحة الأولى: الرئيسية
# ------------------------------------------
if menu == "🏠 الصفحة الرئيسية":
    st.subheader("مرحباً بك في موقع خدمات يونس التجاري")
    st.write("هذا الموقع مصمم خصيصاً لاختبار مهاراتك الأمنية. تجول في الأقسام وابحث عن الثغرات البرمجية!")
    
    st.info("💡 **تلميح للمحقق:** جرب تسجيل الدخول بصلاحيات المدير `admin` بدون معرفة كلمة المرور عبر التلاعب بالمدخلات (SQLi).")

# ------------------------------------------
# الصفحة الثانية: تسجيل الدخول (تحتوي على SQL Injection)
# ------------------------------------------
elif menu == "🔐 تسجيل الدخول":
    st.subheader("تسجيل الدخول إلى حسابك")
    
    username_input = st.text_input("اسم المستخدم:")
    password_input = st.text_input("كلمة المرور:", type="password")
    
    if st.button("دخول"):
        # ⚠️ الثغرة الأولى: ثغرة حقن SQL مباشرة بدون حماية وبدون Prepared Statements!
        query = f"SELECT * FROM users WHERE username = '{username_input}' AND password = '{password_input}'"
        
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            
            if user:
                st.success(f"🎉 تم تسجيل الدخول بنجاح! مرحباً بك يا {user[1]}")
                if user[3] == 1: # إذا كان مدير النظام
                    st.markdown('<div class="flag-box">🚩 FLAG 1 مكتشف: SQL_INJECTION_MASTER_2026</div>', unsafe_allow_html=True)
            else:
                st.error("❌ اسم المستخدم أو كلمة المرور غير صحيحة.")
        except Exception as e:
            st.error(f"حدث خطأ في قاعدة البيانات (خطأ في الاستعلام): {e}")

# ------------------------------------------
# الصفحة الثالثة: التعليقات (تحتوي على Stored XSS)
# ------------------------------------------
elif menu == "💬 قسم التعليقات (Community)":
    st.subheader("آراء المستخدمين والتعليقات")
    
    comment_user = st.text_input("اسمك:", value="زائر")
    new_comment = st.text_area("اكتب تعليقك هنا:")
    
    if st.button("إرسال التعليق"):
        if new_comment:
            # تخزين التعليق كما هو بدون تعقيم أو تنظيف (XSS Vulnerability)
            cursor.execute("INSERT INTO comments (user, comment) VALUES (?, ?)", (comment_user, new_comment))
            conn.commit()
            st.success("تم إرسال تعليقك!")

    st.divider()
    st.markdown("### التعليقات السابقة:")
    cursor.execute("SELECT user, comment FROM comments")
    rows = cursor.fetchall()
    
    for r in rows:
        # ⚠️ الثغرة الثانية: عرض النصوص مباشرة كـ HTML بدون حماية (تسمح بتنفيذ أكواد JavaScript خبيثة)
        st.markdown(f"""
            <div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px; margin-bottom: 8px;">
                <b>{r[0]} قال:</b><br>{r[1]}
            </div>
        """, unsafe_allow_html=True)

    st.info("💡 **تلميح XSS:** جرب كتابة كود جافاسكريبت مصغر داخل التعليق مثل: `<script>alert('XSS Found!')</script>` وانظر ماذا سيحدث!")

# ------------------------------------------
# الصفحة الرابعة: لوحة كشف التحديات
# ------------------------------------------
elif menu == "🕵️‍♂️ لوحة كشف التحديات (Flags)":
    st.subheader("🎯 قائمة التحديات المطلوب اكتشافها في هذا الموقع:")
    
    st.markdown("""
    1. **التحدي الأول (SQL Injection):** حاول الدخول لصفحة المشرف `admin` بدون كلمة مرور عبر استغلال خانة تسجيل الدخول.
    2. **التحدي الثاني (Stored XSS):** اجعل الموقع ينفذ كود تنبيه (`alert`) من خلال خانة التعليقات.
    3. **التحدي الثالث (Information Disclosure):** هل يمكنك معرفة أين يتم حفظ كلمات المرور الخاصة بالمستخدمين الآخرين في الكود أو قاعدة البيانات؟
    """)
    
    st.warning("عندما تكتشف الثغرة، فكر معي: كيف يمكننا **إصلاحها برمجياً** لتأمين هذا الموقع بالكامل؟")
