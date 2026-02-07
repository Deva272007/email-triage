import csv

def classify_email(text):
    text = text.lower()
    if any(k in text for k in ["login", "error", "issue", "problem", "support"]):
        return "Support"
    if any(k in text for k in ["price", "pricing", "purchase", "buy", "sales"]):
        return "Sales"
    if any(k in text for k in ["interview", "hr", "schedule", "job"]):
        return "HR"
    if any(k in text for k in ["win", "prize", "offer", "free", "click"]):
        return "Spam"
    return "General"

def assign_priority(category):
    if category == "Support":
        return "High"
    if category == "Sales":
        return "Medium"
    return "Low"

def route_email(category):
    routes = {
        "Support": "Support Team",
        "Sales": "Sales Team",
        "HR": "HR Team",
        "Spam": "Spam Folder",
        "General": "Inbox"
    }
    return routes.get(category, "Inbox")

input_file = "data/emails.csv"
output_file = "output/results.csv"

with open(input_file, newline="", encoding="utf-8") as infile, \
     open(output_file, "w", newline="", encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)
    fieldnames = ["email_id", "category", "priority", "routed_to"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        content = row["subject"] + " " + row["body"]
        category = classify_email(content)
        priority = assign_priority(category)
        route = route_email(category)

        writer.writerow({
            "email_id": row["email_id"],
            "category": category,
            "priority": priority,
            "routed_to": route
        })

print("Email triage completed. Results saved to output/results.csv")
