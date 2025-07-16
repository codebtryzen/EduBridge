def get_personalized_content(score):
    try:
        score = float(score)
    except ValueError:
        return "Invalid score input."

    if score >= 80:
        return "Advanced content for high performers."
    elif 50 <= score < 80:
        return "Intermediate content to improve your skills."
    else:
        return "Basic content to strengthen your fundamentals."
