from notion_client import Client
import os

notion = Client(auth=os.getenv("NOTION_TOKEN"))
DATABASE_ID = os.getenv("NOTION_DB_ID")

def record_to_notion(data):
    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Timestamp": {"title": [{"text": {"content": data.get("timestamp")}}]},
            "Symbol": {"rich_text": [{"text": {"content": data.get("symbol")}}]},
            "Side": {"select": {"name": data.get("side")}},
            "Entry Price": {"number": data.get("entry_price")},
            "Exit Price": {"number": data.get("exit_price")},
            "Profit": {"number": data.get("profit")},
            "Strategy": {"rich_text": [{"text": {"content": data.get("strategy")}}]}
        }
    )