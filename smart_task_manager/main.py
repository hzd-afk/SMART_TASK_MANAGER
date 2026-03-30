from stt.online_stt import speech_to_text

def run():
    print("\n--- Smart Task Manager ---\n")

    text = speech_to_text()

    if not text:
        print("No input detected")
        return

    print("\nFinal Output:", text)

if __name__ == "__main__":
    run()