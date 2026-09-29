# Sms-Bomb

A Python tool that sends repeated SMS messages to an Indian mobile number, originally built as a prank tool for Termux and Linux.

> **Use responsibly:** Only use this on your own number or with the explicit consent of the recipient. Sending unsolicited messages can violate your carrier's terms and local law. The author is not responsible for misuse.

## What it does

`main.py` takes a target phone number and fires repeated SMS requests through bundled API endpoints. `update.py` handles self-updates of the tool.

## Requirements

- Python 3.8 or newer
- The packages in `requirements.txt` (`requests`, `aiohttp`, `pycryptodome`, `tqdm`, and others)
- A terminal — or [Termux](https://f-droid.org/repo/com.termux_118.apk) on Android

## Install

### 1. Download the project

```bash
git clone https://github.com/kunal4060/Sms-Bomb.git
cd Sms-Bomb
```

### 2. Install the Python packages

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

Follow the on-screen prompts to enter the target number. On Termux, install dependencies first:

```bash
pkg install git python -y
pip install -r requirements.txt
```

## Troubleshooting

### Termux from the Play Store is outdated

The Play Store build of Termux no longer receives updates. Install the latest APK from F-Droid instead: <https://f-droid.org/repo/com.termux_118.apk>

### `ModuleNotFoundError`

Install the requirements with the same Python you run the script with:

```bash
python3 -m pip install -r requirements.txt
```

## License

Provided for educational purposes only. No warranty is provided.
