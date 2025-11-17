from qrng.runner import run_qrng
import string

class QuantumPasswordManager:
    def __init__(self):
        # Define character sets for password generation
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate_password(self, length: int = 12, 
                         use_lowercase: bool = True,
                         use_uppercase: bool = True, 
                         use_digits: bool = True,
                         use_symbols: bool = False) -> str:
        """
        Generate a random password using quantum randomness:        
        Args:
            length (int): Length of the password
            use_lowercase (bool): Include lowercase letters
            use_uppercase (bool): Include uppercase letters  
            use_digits (bool): Include digits
            use_symbols (bool): Include symbols
            
        Returns:
            str: Generated password
        """
        # Build character set based on options
        char_set = ""
        if use_lowercase:
            char_set += self.lowercase
        if use_uppercase:
            char_set += self.uppercase
        if use_digits:
            char_set += self.digits
        if use_symbols:
            char_set += self.symbols
            
        if not char_set:
            raise ValueError("At least one character type must be selected")
            
        # Generate random indices using QRNG
        indices = run_qrng(num_outcomes=len(char_set), shots=length)
        
        # Build password from selected characters
        password = ''.join(char_set[i] for i in indices)
        return password
    
    def generate_multiple_passwords(self, count: int = 5, **kwargs) -> list:
        """
        Generate multiple passwords at once.
        
        Args:
            count (int): Number of passwords to generate
            **kwargs: Arguments passed to generate_password
            
        Returns:
            list: List of generated passwords
        """
        passwords = []
        for i in range(count):
            password = self.generate_password(**kwargs)
            passwords.append(password)
        return passwords

def main():
    """Example usage of the Quantum Password Manager"""
    manager = QuantumPasswordManager()
    
    print("=== Quantum Password Manager ===")
    print("Generating passwords using quantum randomness...\n")
    
    # Generate a strong password
    password = manager.generate_password(
        length=16,
        use_lowercase=True,
        use_uppercase=True, 
        use_digits=True,
        use_symbols=True
    )
    print(f"Strong Password: {password}")
    
    # Generate multiple passwords
    print("\nMultiple passwords:")
    passwords = manager.generate_multiple_passwords(
        count=3,
        length=12,
        use_lowercase=True,
        use_uppercase=True,
        use_digits=True,
        use_symbols=False
    )
    
    for i, pwd in enumerate(passwords, 1):
        print(f"Password {i}: {pwd}")

if __name__ == "__main__":
    main()
