# 🏗️ **Diagrammes d'Architecture Athalia**

## 📊 **Architecture Core**

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor': '#ff6b6b', 'primaryTextColor': '#fff', 'primaryBorderColor': '#ff4757', 'lineColor': '#5f27cd', 'secondaryColor': '#009432', 'tertiaryColor': '#fff'}}}%%
graph TB
    subgraph "🏗️ CORE ARCHITECTURE"
        UO[Unified Orchestrator<br/>Main Coordinator]
        SV[Security Validator<br/>Security Engine]
        PG[Project Generator<br/>Template Engine]
        AC[Auto Cleaner<br/>Cleanup Engine]
    end
    
    subgraph "🛡️ SECURITY LAYER"
        CV[Command Validation<br/>62 secure commands]
        SA[Security Auditing<br/>Dynamic validation]
        IP[Injection Protection]
    end
    
    subgraph "🔧 AUTOMATION"
        AT[Auto Tester<br/>Test Automation]
        AD[Auto Documenter<br/>Doc Generator]
        CM[Cache Manager<br/>Cache Engine]
    end
    
    UO --> SV
    UO --> PG
    UO --> AC
    SV --> CV
    SV --> SA
    SV --> IP
    UO --> AT
    UO --> AD
    UO --> CM
    
    style UO fill:#ff6b6b
    style SV fill:#5f27cd
    style PG fill:#009432
    style AC fill:#ffa502
```

## 🔄 **Workflow de Développement**

```mermaid
gitgraph
    commit id: "Initial Setup"
    branch feature/security
    checkout feature/security
    commit id: "Security Validator"
    commit id: "Command Whitelist"
    checkout main
    merge feature/security
    branch feature/automation
    checkout feature/automation
    commit id: "Auto Cleaner"
    commit id: "Auto Tester"
    checkout main
    merge feature/automation
    commit id: "v12.0.0 Release"
```

## 📚 **Structure de Documentation**

```mermaid
mindmap
  root((📚 Docs))
    👤 Users
      🚀 Quick Start
      📖 User Guide
      ❓ FAQ
      🔧 Troubleshooting
    👨‍💻 Developers
      🏗️ Architecture
      🔍 API Reference
      🤝 Contributing
      🧪 Testing
    🎯 Specialized
      🛡️ Security
      📊 Analytics
      🤖 Automation
      📈 Performance
```

---

*Dernière mise à jour : 21 août 2025*
