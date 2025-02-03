from flask import Flask, render_template, request

app = Flask(__name__)

# Список вопросов
questions = [
    {
        "question": "Жоғары политехникалық колледжде қай мамандық ең көп оқытылады?",
        "options": [
            "Радиотехника, электроника және телекоммуникациялар",
            "Ақпараттық қауіпсіздік жүйелері",
            "Газбен жабдықтар мен жүйелер",
            "Бағдарламалық қамт."
        ],
        "answer": 3
    },
    {
        "question": "Қай жылы жоғары политехникалық колледж ашылды?",
        "options": ["1994", "2000", "2005", "2010"],
        "answer": 0
    },
    {
        "question": "Қай мамандықта студенттер ақпараттық қауіпсіздік жүйелерін меңгереді?",
        "options": [
            "Ақп. жүйелер технигі",
            "Бағдарламалық қамтамасыз ету құрастырушысы",
            "Радиотехника, электроника және телекоммуникациялар",
            "Автомобиль көлігіне техникалық қызмет көрсету"
        ],
        "answer": 0
    },
    {
        "question": "Жоғары политехникалық колледждің кітапханасы қандай мақсаттарға қызмет етеді?",
        "options": [
            "Оқушыларға білім беру және оқулықтарды ұсыну",
            "Әдістемелік көмектер мен зерттеулерді қамтамасыз ету",
            "Ақпараттық ресурстарды тиімді пайдалану",
            "Барлығы"
        ],
        "answer": 3
    },
    {
        "question": "Жоғары политехникалық колледжде қандай мамандықтар оқытылады?",
        "options": [
            "Радиотехника, электроника және телекоммуникациялар",
            "Ақпараттық қауіпсіздік жүйелері",
            "Газбен жабдықтар мен жүйелер",
            "Барлығы"
        ],
        "answer": 3
    }
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        for i, q in enumerate(questions):
            if request.form.get(f"q{i}") == str(q["answer"]):
                score += 1
        return render_template("result.html", score=score, total=len(questions))
    return render_template("quiz.html", questions=questions)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

