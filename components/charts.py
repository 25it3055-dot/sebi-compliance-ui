import plotly.express as px

def pie_chart():
    labels = ["Completed", "Pending", "High Risk"]
    values = [13, 12, 4]

    fig = px.pie(
        names=labels,
        values=values,
        hole=0.5,
        title="Compliance Status"
    )

    return fig


def bar_chart():
    categories = ["KYC", "Policy", "Training", "Audit"]
    values = [8, 5, 6, 3]

    fig = px.bar(
        x=categories,
        y=values,
        title="Tasks by Category"
    )

    return fig