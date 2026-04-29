# 🎲 Provably Fair Dice Game  

**A transparent, verifiable, and secure casino dice game built with Python 3.**  

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)  
![GitHub repo size](https://img.shields.io/github/repo-size/yourusername/casino-development-platform)  

---

## 🔍 Overview  
This repository contains a **provably fair dice game** where players can:  
- 🎯 Bet on "over" or "under" a target number (1-99).  
- 🔒 Verify every roll’s fairness using cryptographic hashing (SHA-256).  
- 📜 Track game history for transparency.  

Built for **casino developers**, **blockchain enthusiasts**, and **gaming platforms**.  

---

## ✨ Features  
✅ **Provably Fair Mechanics**  
- Uses `SHA-256` to generate rolls from combined **player + server seeds**.  
- Players can independently verify rolls with `verify_roll()`.  

✅ **Flexible Betting System**  
- Dynamic payouts based on target risk (e.g., betting "over 75" pays 4x).  

✅ **Game History Logging**  
- Saves all rolls, bets, and outcomes in JSON format.  

✅ **Terminal & Web-Ready**  
- Playable via CLI (terminal) or extendable to **Flask/Django**.  

✅ **MIT Licensed**  
- Free for commercial and personal use.  

---

## 🛠 Installation  
1. Clone the repo:  
   ```bash  
   git clone https://github.com/mayhymn0890/open-casino-dev.git  
   cd casino-development-platform/games  
   ```  

2. Run the game:  
   ```bash  
   python3 provably_fair_dice.py  
   ```  

---

## 🎮 How to Play  
1. **Set Your Seed**:  
   - Enter any string (e.g., `"player123"`) as your seed.  

2. **Place a Bet**:  
   ```  
   Bet amount: $10  
   Target (1-99): 50  
   Bet 'over' (o) or 'under' (u)? o  
   ```  

3. **View Results**:  
   ```  
   🎯 Rolled: 63  
   🔑 Hash: a1b2c3...  
   ✅ You won $19.80!  
   ```  

4. **Verify Fairness**:  
   - Recompute the hash using the provided seeds to confirm the roll was untampered.  

---

## 📂 Repository Structure  
```  
.  
├── games/  
│   └── provably_fair_dice.py  # Main game script  
├── LICENSE  
└── README.md  
```  

---

## 🔧 Extending the Project  
### **1. Add Blockchain Verification**  
Modify `verify_roll()` to check against an **Ethereum smart contract**:  
```python  
from web3 import Web3  
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io"))  

def verify_on_blockchain(self, roll_hash: str) -> bool:  
    contract = w3.eth.contract(address="0x...", abi=...)  
    return contract.functions.verifyRoll(roll_hash).call()  
```  

### **2. Web Interface**  
Wrap the game in **Flask**:  
```python  
from flask import Flask, request  
app = Flask(__name__)  

@app.route("/roll", methods=["POST"])  
def roll():  
    bet = request.json["bet"]  
    target = request.json["target"]  
    return game.roll(bet, target)  
```  

---

## 🤝 Contributing  
1. Fork the repo.  
2. Add new games (e.g., **roulette**, **slots**, **blackjack**).  
3. Submit a PR!  

---

## 📜 License  
MIT © 2024 [Your Name]  

---
