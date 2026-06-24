def format_sources(sources):
    if not sources:
        return "No sources available."
    formatted = "**📚 Key Sources:**\n\n"
    seen = set()
    for doc in sources:
        source = doc.metadata.get('source', 'Document').replace('data\\', '').replace('data/', '')
        if source not in seen:
            seen.add(source)
            formatted += f"• {source}\n"
    return formatted

def get_emergency_contacts():
    return """
**Andhra Pradesh Wildlife Emergency Contacts:**

- **State Wildlife Helpline**: 1926
- **AP Forest Department Control Room**: 0866-241XXXX (Check latest)
- **Local Forest Range Officer**: Contact your nearest Forest Office
- **Police Emergency**: 100
    """