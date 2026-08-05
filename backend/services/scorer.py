import re

def calculate_score(candidate, job):

    score = 0

    matched = []
    missing = []

    required_skills = [
        skill.strip().lower()
        for skill in job["requiredSkills"].split(",")
        if skill.strip()
    ]

    candidate_skills = [
        skill.lower()
        for skill in candidate.get("skills", [])
    ]

    # Required Skills (70 Marks)
    if required_skills:

        points = 70 / len(required_skills)

        for skill in required_skills:

            if skill in candidate_skills:
                score += points
                matched.append(skill)
            else:
                missing.append(skill)

    # Experience (20 Marks)
    candidate_exp = candidate.get("experience", "").lower()

    if job["experience"] == "0":
        score += 20

    elif "fresher" in candidate_exp:
        score += 0

    else:
        match = re.search(r"\d+", candidate_exp)

        if match:
            years = int(match.group())

            if years >= int(job["experience"]):
                score += 20

    # Projects (10 Marks)
    if candidate.get("projects"):
        score += 10

    # Recommendation
    recommendation = "Not Suitable"

    if score >= 85:
        recommendation = "Strong Fit"
    elif score >= 70:
        recommendation = "Good Fit"
    elif score >= 50:
        recommendation = "Moderate Fit"

    return {
        "score": round(score),
        "matchedSkills": matched,
        "missingSkills": missing,
        "recommendation": recommendation
    }