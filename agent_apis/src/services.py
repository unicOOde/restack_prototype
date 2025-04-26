import asyncio
import logging
import webbrowser
from pathlib import Path

from watchfiles import run_process

from src.client import client
from src.functions.llm import llm
from src.functions.weather import weather
from src.workflows.multistep import MultistepWorkflow


async def main() -> None:
    await client.start_service(
        workflows=[MultistepWorkflow],
        functions=[llm, weather],
    )


def run_services() -> None:
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Service interrupted by user. Exiting gracefully.")


def watch_services() -> None:
    watch_path = Path.cwd()
    logging.info("Watching %s and its subdirectories for changes...", watch_path)
    webbrowser.open("http://localhost:5233")
    run_process(watch_path, recursive=True, target=run_services)


if __name__ == "__main__":
    run_services()
