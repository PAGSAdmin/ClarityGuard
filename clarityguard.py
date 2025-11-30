# ClarityGuard — the TruthSleuth — FINAL WORKING VERSION — 2025-11-30
# Created by PAGS — 40 years turning chaos into clarity

import re

def clarityguard(text: str):
    impact = count_impact(text)
    story = classify_story(text)
    guard = clarity_guard(text)

    output = {
        "impact": impact,
        "story": story,
        "guard": guard,
        "grade": calculate_grade(guard, story, text, impact),
        "one_breath": generate_one_breath(impact, story, guard, text),
        "paraphrase": text.strip(),
        "insight": generate_insight(text, impact, story, guard),
        "math": generate_math(text, impact),
        "learn_more": generate_learn_more(text, story, impact),
        "relevance": generate_relevance(story, impact, text),
    }

    return format_output(output, impact["cat"] > 0, text)


def count_impact(t: str) -> dict:
    t_lower = t.lower()
    deaths = sum(int(x) for x in re.findall(r'\b(\d+)\b.*?(dead|died|death|killed|fatal)', t_lower) or [0])
    affected = sum(int(x) for x in re.findall(r'\b(\d+)\b.*?(hospital|injured|case|affected|infection|evacuated?|trapped|displaced)', t_lower) or [0])
    score = deaths * 15 + affected
    if deaths >= 100 or affected >= 10000: return {"cat": 5, "desc": f"Catastrophic — {deaths} deaths"}
    if deaths >= 10 or affected >= 1000: return {"cat": 4, "desc": "Severe — thousands affected"}
    if deaths >= 3 or affected >= 100: return {"cat": 3, "desc": "Major regional crisis"}
    if affected >= 10: return {"cat": 2, "desc": "Regional disruption"}
    if score >= 5: return {"cat": 1, "desc": "Local incident"}
    return {"cat": 0, "desc": ""}


def classify_story(t: str) -> dict:
    t_lower = t.lower()
    if any(k in t_lower for k in ["tax","policy","vote","election","law","bill","senate","congress","war","trump","putin","israel","border","judge"]):
        return {"bucket": "POLITICS"}
    if any(k in t_lower for k in ["health","food","parent","child","brain","psychology","history","science","geography","diet"]):
        return {"bucket": "UNDERSTANDING"}
    if any(k in t_lower for k in ["study","research","data","trial","paper","found","linked","%"]):
        return {"bucket": "ANALYSIS"}
    if any(k in t_lower for k in ["meme","lol","funny","joke","game","sport","puppy"]):
        return {"bucket": "FUN"}
    return {"bucket": "none"}


def clarity_guard(t: str) -> dict:
    t_lower = t.lower()
    if any(p in t_lower for p in ["5g covid","microchip","flat earth","chemtrails","deep state"]):
        return {"type": "CONSPIRACY"}
    if len(re.findall(r'\b[A-Z]{4,}\b', t)) > 3 or t.count('!') > 5:
        return {"type": "RANT"}
    if re.search(r"(poison|toxic).{0,30}(trace|tiny|seed).{0,20}(deadly|kills?)", t_lower):
        return {"type": "DOSE FALLACY"}
    return {"type": "Pass"}


def calculate_grade(guard, story, text: str, impact) -> str:
    if guard["type"] != "Pass":
        return "C"
    if impact["cat"] > 0 or any(k in text.lower() for k in ["official","confirmed","death toll","police say","witness","i was","my experience","happened to me"]):
        return "A"
    return "B"


def generate_insight(t, i, s, g):
    t_lower = t.lower()
    if i["cat"] > 0: return "Real population impact — verify latest official numbers."
    if "apple" in t_lower: return "You would need to chew ~200 apple seeds in one sitting for any risk. Dose makes the poison."
    if s["bucket"] == "ANALYSIS": return "Derived claim — always check primary study + absolute risk."
    if g["type"] != "Pass": return f"{g['type']} stripped — truth remains."
    return "Clear perspective delivered."

def generate_one_breath(i, s, g, t):
    if i["cat"] > 0: return "Real emergency."
    if "apple" in t.lower(): return "Truth: dose makes the poison."
    if s["bucket"] == "ANALYSIS": return "Check absolute risk, not just percent."
    if g["type"] != "Pass": return f"{g['type']} stripped — truth left."
    return "Clear take."

def generate_math(t, i):
    return ""

def generate_learn_more(t, s, i):
    return "Ask any AI: “Tell me more about the core claim here.”"

def generate_relevance(s, i, t):
    if i["cat"] > 0: return "EMERGENCY"
    if s["bucket"] == "UNDERSTANDING": return "Health"
    if s["bucket"] == "POLITICS": return "Politics"
    if s["bucket"] == "FUN": return "Fun"
    return "General"


def format_output(o, show_impact, text):
    lines = ["**ClarityGuard — the TruthSleuth**", "Created by PAGS", ""]

    # Population Impact Factor + Siren / Warning
    if show_impact:
        shield = "\U0001F6A8" if o["impact"]["cat"] >= 4 else "\u26A0\uFE0F"
        lines.append(f"{shield} Population Impact Factor: Cat {o['impact']['cat']}")
        lines.append(o["impact"]["desc"])
        if o["impact"]["cat"] >= 4:
            lines.append("EMERGENCY WARNING")
        lines.append("")

    # Category with emoji and explanation
    bucket_icons = {"POLITICS":"\u2696\uFE0F", "UNDERSTANDING":"\U0001F4A1", "ANALYSIS":"\U0001F4C8", "FUN":"\U0001F389"}
    if o["story"]["bucket"] != "none":
        lines.append(f"{bucket_icons.get(o['story']['bucket'], '')} Category: {o['story']['bucket']}")
        lines.append({"POLITICS":"(power, law, war, elections, government)",
                      "UNDERSTANDING":"(health, science, history, parenting — anything we want to learn)",
                      "ANALYSIS":"(studies, percentages, “research says”)",
                      "FUN":"(joy, jokes, memes, sports, celebration)"}.get(o["story"]["bucket"], ""))

    # Claim From + Subject
    lines.append(f"Claim From: {'Official / Eyewitness / Personal Experience' if o['grade']=='A' else 'Studies / Reports / Experts' if o['grade']=='B' else 'Rant / Conspiracy / Dose Fallacy'} → {o['grade']}")
    lines.append(f"Subject: #{o['relevance']} ✨")
    lines += ["", "Paraphrase:", o["paraphrase"], ""]
    lines.append("Insight:")
    lines.append(o["insight"])
    lines += ["", "One breath, one truth:", o["one_breath"], ""]
    lines.append(f"Learn more → {o['learn_more']}")
    lines.append(f"\n*Verdict: You just chose clarity. TruthSleuth delivered.*")
    lines += ["", "Truth with heart",
              "Created by PAGS — 40 years turning chaos into clarity",
              "Your clarity. Your control."]

    return "\n".join(lines)

if __name__ == "__main__":
    test = input("Paste any story → ")
    print("\n" + clarityguard(test))
    input("\nPress Enter to close...")
