import hashlib
import random
import json
from typing import Dict, Optional

class ProvablyFairDice:
    """
    A provably fair dice game using SHA-256 hashing.
    Players can verify fairness using seeds.
    """
    
    def __init__(self, server_seed: Optional[str] = None):
        self.server_seed = server_seed or self._generate_seed()
        self.player_seed = None
        self.game_history = []
        
    def _generate_seed(self) -> str:
        """Generate a random server seed."""
        return hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()
    
    def set_player_seed(self, player_seed: str) -> None:
        """Set the player's seed (can be any string)."""
        self.player_seed = player_seed
    
    def roll(self, bet: float, target: int, over: bool = True) -> Dict:
        """
        Roll the dice and determine win/loss.
        
        Args:
            bet (float): Amount wagered.
            target (int): Target number (1-100).
            over (bool): Bet on over (True) or under (False).
        
        Returns:
            Dict: Game result (win/loss, roll, hash, etc.).
        """
        if not self.player_seed:
            raise ValueError("Player seed not set!")
        
        combined_seed = f"{self.player_seed}-{self.server_seed}"
        roll_hash = hashlib.sha256(combined_seed.encode()).hexdigest()
        roll = int(roll_hash[:8], 16) % 100 + 1  # 1-100

        is_win = (over and roll > target) or (not over and roll < target)
        payout = bet * (99 / (100 - target)) if is_win else 0
        
        result = {
            "roll": roll,
            "server_seed": self.server_seed,
            "player_seed": self.player_seed,
            "hash": roll_hash,
            "bet": bet,
            "target": target,
            "over": over,
            "win": is_win,
            "payout": payout,
        }
        
        self.game_history.append(result)
        return result
    
    def verify_roll(self, player_seed: str, server_seed: str, roll_hash: str) -> bool:
        """Verify a past roll's fairness."""
        combined = f"{player_seed}-{server_seed}"
        return hashlib.sha256(combined.encode()).hexdigest() == roll_hash


if __name__ == "__main__":
    game = ProvablyFairDice()
    print("🎲 Provably Fair Dice Game 🎲")
    print(f"Server Seed: {game.server_seed}\n")
    
    game.set_player_seed(input("Enter your seed: "))
    balance = 1000.0
    
    while balance > 0:
        print(f"\nBalance: ${balance:.2f}")
        try:
            bet = float(input("Bet amount: $"))
            target = int(input("Target (1-99): "))
            over = input("Bet 'over' (o) or 'under' (u)? ").lower() == "o"
            
            if bet > balance:
                print("Not enough balance!")
                continue
            
            result = game.roll(bet, target, over)
            print(f"\n🎯 Rolled: {result['roll']}")
            print(f"🔑 Hash: {result['hash']}")
            
            if result["win"]:
                balance += result["payout"]
                print(f"✅ You won ${result['payout']:.2f}!")
            else:
                balance -= bet
                print("❌ You lost!")
            
            # Verify fairness (demo)
            if game.verify_roll(result["player_seed"], result["server_seed"], result["hash"]):
                print("🔒 Fairness verified!")
            else:
                print("⚠️ Verification failed!")
                
        except ValueError:
            print("Invalid input!")
    
    print("\n💸 Game over! You're out of funds.")
    print("Game History:")
    print(json.dumps(game.game_history, indent=2))
