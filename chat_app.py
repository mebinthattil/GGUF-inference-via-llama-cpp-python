#Chat app plugin for gguf_inference.py
from gguf_inference import load_gguf_model

def main():
    model_path = "/Users/mebin/Downloads/Work/Coding Projects/sugar-dev/AI/LlaMA 135 Claude RUN2 q4.gguf"
    
    print("Loading model")
    model = load_gguf_model(model_path)  # Mode 1 = temp 0.7
    model.set_generation_mode(3)
    
    print("Chat started! Type 'quit' to exit.\n")
    
    while True:
        user_input = input("input: ").strip()
        
        if user_input.lower() == 'quit':
            break
            
        if not user_input:
            continue
        
        try:
            response = model.ask_question(user_input)
            print(f"response: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")
    
    print("Goodbye!")

if __name__ == "__main__":
    main()

