import sys
import io
import streamlit as st

# ==========================================
# 1. إعدادات الصفحة والتصميم المعاصر 2026 (VIP Glassmorphism)
# ==========================================
st.set_page_config(
    page_title="أكاديمية يونس للبرمجة - Python Lab 2026",
    page_icon="💻",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top right, #2e1065, #09090b 60%, #030014);
        background-attachment: fixed;
        color: #f8fafc;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    .glass-header {
        background: rgba(30, 27, 75, 0.4);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(99, 102, 241, 0.25);
        padding: 24px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    .lesson-card {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.2);
        padding: 20px;
        border-radius: 14px;
        margin-bottom: 20px;
    }
    .code-output {
        background-color: #020617;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 15px;
        font-family: 'Courier New', Courier, monospace;
        color: #38bdf8;
    }
    .stButton>button {
        border-radius: 10px !important;
        background: linear-gradient(135deg, #4f46e5, #3b82f6) !important;
        color: white !important;
        font-weight: 600 !important;
        border: none !important;
        padding: 10px 20px !important;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. قاعدة بيانات الدروس والتحديات البرمجية
# ==========================================
LESSONS = {
    "1. المتغيرات والطباعة (Variables & Print)": {
        "concept": """
        المتغير هو مثل **صندوق** تخزن فيه قيمة (نص، رقم، أو قائمة).
        أمر `print()` يستعمل لعرض وتحذير القيمة على الشاشة.
        """,
        "example": 'name = "يونس"\nage = 16\nprint(f"مرحباً {name}، عمرك {age} سنة!")',
        "task": 'اكتب كوداً ينشئ متغيراً باسم `city` يحتوي على مدينتك، ثم اطبعه باستخدام `print(city)`',
        "expected_keyword": "print"
    },
    "2. الشروط واتخاذ القرار (If / Else)": {
        "concept": """
        تستخدم الشروط لجعل البرنامج يتخذ قرارات مختلفة بناءً على معطيات.
        مثال: إذا كان العمر أكبر من 18، اسمح بدخول الموقع، وإلا ارفض.
        """,
        "example": 'age = 16\nif age >= 18:\n    print("مسموح")\nelse:\n    print("غير مسموح")',
        "task": 'اكتب شرطاً ينظر في متغير `score = 80`؛ إذا كان أكبر من 50 يطبع "ناجح".',
        "expected_keyword": "if"
    },
    "3. الحلقات التكرارية (For Loops)": {
        "concept": """
        تستخدم لتكرار تنفيذ الكود عدة مرات بدون الحاجة لإعادة كتابته.
        """,
        "example": 'for i in range(5):\n    print(f"التكرار رقم: {i+1}")',
        "task": 'اكتب حلقة `for` تطبع الأرقام من 1 إلى 3.',
        "expected_keyword": "for"
    },
    "4. القوائم (Lists)": {
        "concept": """
        القائمة تتيح لك حفظ مجموعة من العناصر أو الأسماء في مكان واحد.
        """,
        "example": 'games = ["Free Fire", "eFootball", "Roblox"]\nprint(games[0]) # يطبع العنصر الأول',
        "task": 'أنشئ قائمة باسم `skills` تحتوي على لغتين برمجيتين واطبع القائمة.',
        "expected_keyword": "print"
    }
}

# ==========================================
# 3. الهيدر والتصميم الرئيسي
# ==========================================
st.markdown("""
    <div class="glass-header">
        <h2 style="margin: 0; font-size: 26px; font-weight: 800; background: linear-gradient(to right, #a5b4fc, #e0e7ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">💻 منصة تعلم البرمجة التفاعلية 2026</h2>
        <p style="margin: 8px 0 0 0; color: #94a3b8; font-size: 14px;">اقرأ الدرس، جرب الكود بنفسك، وحل التحديات البرمجية مباشرة!</p>
    </div>
""", unsafe_allow_html=True)

# الشريط الجانبي اختيار الدرس
with st.sidebar:
    st.markdown("### 📚 المسار التعليمي")
    selected_lesson_name = st.radio("اختر الدرس:", list(LESSONS.keys()))
    st.divider()
    st.info("💡 **نصيحة يونس البرمجية:** البرمجة ليست حفظاً بل تجربة ومحاولة وممارسة!")

current_lesson = LESSONS[selected_lesson_name]

# ==========================================
# 4. عرض المحتوى والتجربة الحية
# ==========================================
col_learn, col_code = st.columns([1, 1.2])

with col_learn:
    st.subheader(f"📖 {selected_lesson_name}")
    
    st.markdown(f'<div class="lesson-card"><b>المفهوم الأساسي:</b><br>{current_lesson["concept"]}</div>', unsafe_allow_html=True)
    
    st.markdown("**مثال توضيحي:**")
    st.code(current_lesson["example"], language="python")
    
    st.markdown("---")
    st.subheader("🎯 التحدي المطلوب:")
    st.warning(current_lesson["task"])

with col_code:
    st.subheader("👨‍💻 محرر الكود والمختبر الحي")
    
    user_code = st.text_area(
        "اكتب كود بايثون هنا لتجربته وتستخرج النتيجة:",
        value=current_lesson["example"],
        height=220
    )
    
    if st.button("🚀 تشغيل الكود واختبار النتيجة"):
        # التقاط المخرجات البرمجية (stdout)
        buffer = io.StringIO()
        sys.stdout = buffer
        
        try:
            # تنفيذ الكود البرمجي بأمان محلي
            exec(user_code)
            sys.stdout = sys.__stdout__
            output = buffer.getvalue()
            
            st.success("✅ تم تنفيذ الكود بنجاح!")
            st.markdown("**مخرجات الكود (Output):**")
            st.code(output if output else "تم تنفيذ الكود بنجاح بدون طباعة نصية.", language="text")
            
            # التحقق من التحدي
            if current_lesson["expected_keyword"] in user_code:
                st.balloons()
                st.toast("ممتاز يا يونس! لقد طبقت فكرة الدرس بنجاح 🔥", icon="🎉")
            
        except Exception as e:
            sys.stdout = sys.__stdout__
            st.error("❌ حدث خطأ في الكود:")
            st.code(str(e), language="python")

