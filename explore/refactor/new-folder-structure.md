# New Project Folder Structure

Below is the directory tree showing the platform-independent core layout.

```
instagram/ (Root)
│
├── core/                       <-- Core Platform-Independent modules
│   ├── config/                 <-- Configuration loaders (Python & JS)
│   │   ├── config.py
│   │   └── config.cjs
│   ├── models/                 <-- Common domain models (dataclasses)
│   │   └── models.py
│   ├── services/               <-- Reusable business operations
│   │   ├── llm_service.py
│   │   └── file_service.py
│   ├── utils/                  <-- Data cleaners & date formatters
│   │   ├── json_helper.py
│   │   └── date_helper.py
│   └── interfaces/             <-- Abstract interfaces for decoupling
│       └── interfaces.py
│
├── adapters/                   <-- Platform adapters namespace
│   └── linkedin/               <-- LinkedIn-specific integrations
│       ├── publisher/
│       ├── scheduler/          <-- Copied scheduling scripts
│       ├── prompts/            <-- Formatting rules
│       └── assets/             <-- HTML templates
│
├── shared/                     <-- Global sharing folder
├── tests/                      <-- Automated unit/integration tests
│
└── explore/                    <-- Audit and refactoring documentation
    └── refactor/               <-- Refactor summaries & logs
```
