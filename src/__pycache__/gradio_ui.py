import pandas as pd
import gradio as gr

from model_training import predict_car_price
from visualization import get_visualization


def filter_cars(df, min_price, max_price, fuel_type, body_style):
    """Filters cars by user selections and returns filtered table + stats."""
    filtered = df[(df['price'] >= min_price) & (df['price'] <= max_price)]

    if fuel_type != "All":
        filtered = filtered[filtered['fuel_type'] == fuel_type]

    if body_style != "All":
        filtered = filtered[filtered['body_style'] == body_style]

    stats = {
        "Total Cars": len(filtered),
        "Petrol Cars": len(filtered[filtered['fuel_type'] == 'gas']),
        "Diesel Cars": len(filtered[filtered['fuel_type'] == 'diesel']),
        "Hatchbacks": len(filtered[filtered['body_style'] == 'hatchback'])
    }

    stats_df = pd.DataFrame(list(stats.items()), columns=["Category", "Count"])

    out_df = filtered[["make", "body_style", "fuel_type", "engine_size", "horsepower", "price"]] \
        .sort_values(by="price")

    return out_df, stats_df


def build_app(df, features, model):
    """Creates and returns the Gradio Blocks app."""
    with gr.Blocks(theme=gr.themes.Soft(primary_hue="orange", font=["Verdana", "Arial", "sans-serif"])) as demo:
        gr.Markdown("""
        <div style='text-align:center;'>
            <img src='https://cdn-icons-png.flaticon.com/512/743/743008.png' width='80'/>
            <h1 style='color:#FF7F00; font-family:Verdana;'>🚗 Car Price Prediction Dashboard</h1>
            <p style='font-size:16px;'>✨ Predict car prices, explore features, and visualize insights ✨</p>
        </div>
        """)

        # ----------------- Predict Tab -----------------
        with gr.Tab("🔮 Predict Car Price"):
            with gr.Accordion("Enter Car Specifications", open=True):
                with gr.Row():
                    nl = gr.Number(label="Normalized Losses", value=100)
                    wb = gr.Number(label="Wheel Base", value=95)
                    es = gr.Number(label="Engine Size", value=130)
                    bore = gr.Number(label="Bore", value=3.2)
                    stroke = gr.Number(label="Stroke", value=3.0)
                with gr.Row():
                    cr = gr.Number(label="Compression Ratio", value=9.0)
                    hp = gr.Number(label="Horsepower", value=120)
                    rpm = gr.Number(label="Peak RPM", value=5200)

            predict_btn = gr.Button("🔍 Predict Now", variant="primary")
            price_output = gr.Number(label="Predicted Price (USD)", interactive=False)

            def _predict(nl, wb, es, bore, stroke, cr, hp, rpm):
                return predict_car_price(model, nl, wb, es, bore, stroke, cr, hp, rpm)

            predict_btn.click(fn=_predict, inputs=[nl, wb, es, bore, stroke, cr, hp, rpm], outputs=price_output)

        # ----------------- Visual Insights Tab -----------------
        with gr.Tab("📊 Visual Insights"):
            chart_selector = gr.Dropdown(
                choices=[
                    "Price Distribution",
                    "Correlation Heatmap",
                    "Fuel Type vs Price",
                    "Top 10 Car Makes by Avg Price",
                    "Horsepower vs Price",
                    "Engine Size vs Price",
                    "Body Style vs Price",
                    "Drive Type vs Price",
                    "Make vs Price"
                ],
                label="Select a Chart",
                value="Price Distribution"
            )
            chart_output = gr.Plot()

            def _show_chart(chart_type):
                return get_visualization(df, features, chart_type)

            chart_selector.change(fn=_show_chart, inputs=chart_selector, outputs=chart_output)

        # ----------------- Filter Cars Tab -----------------
        with gr.Tab("🎯 Filter Cars"):
            gr.Markdown("<h3 style='color:#FF7F00;'>Filter Cars by Attributes</h3>")

            min_p = gr.Number(label="Minimum Price ($)", value=5000)
            max_p = gr.Number(label="Maximum Price ($)", value=20000)
            fuel_filter = gr.Dropdown(
                choices=["All"] + sorted(df['fuel_type'].dropna().unique()),
                label="Fuel Type",
                value="All"
            )
            body_filter = gr.Dropdown(
                choices=["All"] + sorted(df['body_style'].dropna().unique()),
                label="Body Style",
                value="All"
            )

            filter_btn = gr.Button("Filter Now")
            filter_table = gr.Dataframe()
            stats_table = gr.Dataframe(label="Filter Statistics")

            def _filter(min_price, max_price, fuel_type, body_style):
                return filter_cars(df, min_price, max_price, fuel_type, body_style)

            filter_btn.click(
                fn=_filter,
                inputs=[min_p, max_p, fuel_filter, body_filter],
                outputs=[filter_table, stats_table]
            )

    return demo
