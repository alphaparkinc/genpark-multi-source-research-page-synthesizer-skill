from client import MultiSourceResearchSparkPageSynthesizerClient

def main():
    client = MultiSourceResearchSparkPageSynthesizerClient()
    res = client.synthesize_research_page("Quantum Computing Commercial Readiness 2026", 10)
    print(f"Fact Score: {res['fact_score']}")
    print(f"Sources Indexed: {res['sources_indexed']}")
    print(res["synthesized_page_md"])

if __name__ == "__main__":
    main()
