from app.agent import run_agent

print("AI Agent started. Type 'exit' to stop.\n")

while True:
    q = input("Ask a question: ")

    if q.lower() == "exit":
        print("Exiting AI Agent...")
        break

    answer = run_agent(q, session_id="user1")
    print("\nAnswer:\n", answer)
    print("-" * 50)
