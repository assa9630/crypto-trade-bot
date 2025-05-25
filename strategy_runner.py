from trade_manager import run_trade_logic
from apscheduler.schedulers.background import BackgroundScheduler

def run_strategy():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_trade_logic, "interval", minutes=15)
    scheduler.start()