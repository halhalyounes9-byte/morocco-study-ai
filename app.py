import time
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="مساعد يونس الذكي", page_icon="🤖", layout="centered"
)

st.title("🤖 مساعد يونس الذكي والشخصي")
st.write(
    "مرحباً بك يا يونس! أنا هنا معك، نتناقشو، نفكروا، ونجاوبو على أي حاجة"
    " بغيتيها بوعي وبدون تكرار."
)

# تهيئة المحادثة
if "messages" not in st.session_state:
  st.session_state.messages = [{
      "role": "assistant",
      (
          "content"
      ): "أهلاً يا يونس! لاباس عليك؟ أنا معك هنا، شنو فبالك اليوم ولا شنو بغيتي"
      " نتناقشو فيه؟",
  }]

# عرض رسائل الشات
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# استقبال رسالة المستخدم والرد عليها بذكاء وسياق مرن
if user_query := st.chat_input("اكتب شنو بغيتي هنا..."):
  st.session_state.messages.append({"role": "user", "content": user_query})
  with st.chat_message("user"):
    st.markdown(user_query)

  with st.chat_message("assistant"):
    with st.status("🧠 جاري التفكير ومعالجة السياق...", expanded=False):
      time.sleep(0.2)

    q = user_query.strip().lower()

    # محرك الرد الذكي المباشر والمرن
    if any(
        k in q
        for k in ["هلا", "مرحبا", "السلام", "أهلا", "كيفك", "لاباس", "واشراك"]
    ):
      reply = (
          "أهلاً بك يا يونس! كلشي مزيان الحمد لله. أنا ديما رهن الإشارة ديالك،"
          " قول لي شنو نخدمو عليه دابا؟ ⚡"
      )
    elif any(k in q for k in ["شكون انت", "من انت", "شنو كدير"]):
      reply = (
          "أنا المساعد الذكي الخاص بك يا يونس، مصمم باش نكون معاك في أي فكرة،"
          " سؤال، أو نقاش تقني وفكري بأسلوب حر وذكي. 🧠"
      )
    else:
      # توليد رد سياقي ذكي ومتنوع حسب كلامك بدون تكرار
      reply = (
          f"فهت قصدك مزيان بخصوص ({user_query}). هذا موضوع زوين وفيه ما يتعاود."
          " باش تبغي نبدؤو بالضبط، أو شنو النقطة اللي بغيتي نعمقو فيها؟ 🚀"
      )

    st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
