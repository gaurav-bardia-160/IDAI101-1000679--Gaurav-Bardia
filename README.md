[![Platform](https://img.shields.io/badge/Platform-Google%20Dialogflow%20ES-orange.svg)](https://dialogflow.cloud.google.com/)
[![Integration](https://img.shields.io/badge/Integration-Telegram%20Bot%20API-blue.svg)](https://core.telegram.org/bots)
[![Python Version](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Deployment-Live-success.svg)]()

---

## 📋 Student Details

| Field                             | Details                                                           |
| --------------------------------- | ----------------------------------------------------------------- |
| **Student Full Name**             | Gaurav Gautam Bardia                                              |
| **Candidate Registration Number** | `1000679`                                                         |
| **Course Name**                   | Artificial Intelligence: Real-World Applications and Implications |
| **CRS Name**                      | Artificial Intelligence (CRS: AI)                                 |
| **School Name**                   | Udgam School For Children                                         |

---

## 🔗 Live Chatbot Links

* **Live Interactive Telegram Bot:** [Open Telegram Bot](https://web.telegram.org/a/#8894929465)

## 🔗 Model Demo Video
* **Google Drive videolink:** [Open Google Drive](https://drive.google.com/drive/folders/1uYh_heDqxb5qFXlBqyMm8Rx8nRjDnors)

---

# 📌 1. Project Overview

Digital financial ecosystems face an escalating volume of fraud vectors, including:

* UPI collect-request scams
* Fake KYC blocks
* Task-based work-from-home fraud
* Coercive "Digital Arrest" extortion calls
* Phishing links
* Fake payment notifications
* Impersonation scams

**ScamShield AI** is an intelligent conversational safety assistant engineered using **Google Dialogflow ES**.

Its primary objectives are to:

* Classify potential fraud scenarios
* Identify common scam indicators
* Educate users about emerging threats
* Provide safety-oriented recommendations
* Guide users through post-scam recovery workflows
* Provide context-aware responses during multi-step interactions

---

## 🎯 Target Demographics & User Needs

### 💳 Digital Banking & UPI Users

ScamShield AI helps users identify:

* Fake payment screenshots
* Unauthorized card transactions
* Fraudulent UPI requests
* Phishing links
* Fake banking notifications

### 💼 Job Seekers & Students

The chatbot addresses:

* Upfront-fee recruitment scams
* Fake work-from-home opportunities
* Task-based scams
* Fake Telegram recruitment
* Suspicious loan applications

### 👴 Vulnerable & Elderly Users

The system provides guidance for high-pressure scams such as:

* Law-enforcement impersonation
* Digital arrest scams
* Emergency impersonation
* AI voice-cloning threats

---

# 🧠 2. Dialogflow Intents & Entities

## 2.1 Intent Taxonomy

The agent contains **85 production intents** organized into several functional groups.

### Legitimate Communication Filter

#### `00_legitimate_communication`

Identifies potentially legitimate communications, including:

* Banking transaction notifications
* HDFC/Axis transaction alerts
* Official courier tracking updates

This intent helps reduce false-positive scam classifications.

---

## Direct Threat Detection — Intents `01–55`

These intents analyze SMS messages, email transcripts, and chat messages for active fraud indicators.

### Banking & Financial Fraud

* `bank_phishing`
* `upi_fraud`
* `credit_card_theft`
* `tax_agency_fraud`
* `pf_epfo_withdrawal_scam`
* `credit_card_reward_points`

### Extortion & Impersonation

* `digital_arrest`
* `police_impersonation`
* `customs_clearance`
* `deepfake_video_extortion`
* `sextortion`
* `fake_courier_drugs_extortion`

### Device & Account Takeover

* `tech_support`
* `remote_access_takeover`
* `sim_swap`
* `otp_bypass`
* `e_sim_swapping_fraud`
* `free_wifi_hacking`

### Social Engineering & Recruitment

* `task_based_scam`
* `work_from_home_fraud`
* `fake_job_interview_telegram`
* `mule_account_recruitment`
* `social_engineering_isolation`

### Marketplace & E-Commerce

* `marketplace_buyer_fraud`
* `marketplace_seller_fraud`
* `delivery_fee_scam`
* `brushing_scam_amazon`
* `fake_concert_event_ticket`

### Investment & Cryptocurrency Schemes

* `crypto_investment`
* `pig_butchering`
* `crypto_drainer_airdrop`
* `fake_crypto_exchange_kyc`
* `crypto_cloud_mining`

---

## Scam Education & Early Signs — Intents `56–70`

These intents provide educational responses about:

* Comprehensive awareness guide detailing the 5 universal scam red flags (Artificial Urgency, Forced Isolation, Irregular Payments, Credential Requests, and Unrealistic Gains).
* Outlines major localized fraud vectors in India (Digital Arrest, UPI collect traps, electricity shutoff threats, KYC deactivation, predatory loan apps, and EPFO refund phishing).
* Covers top global cybercrime threats (Telegram review/task traps, Pig Butchering crypto schemes, AI voice cloning, delivery smishing, and CEO business email compromise).

---

## Post-Scam Recovery Playbooks — Intents `71–85`

The chatbot includes five context-gated recovery pipelines.

### 💰 Financial Recovery

`recv_fin`

Provides guidance for:

* Card freezing
* Financial incident response
* Dispute-related actions

### 👮 Legal & Police Recovery

`recv_pol`

Provides guidance related to:

* Reporting suspected cybercrime
* National Cybercrime Helpline `1930`
* Cybercrime portal registration

### 🪪 Identity & Account Recovery

`recv_id`

Provides guidance for:

* Terminating active sessions
* Securing compromised accounts
* Setting up two-factor authentication

### 💻 Device & Malware Recovery

`recv_dev`

Provides guidance for:

* Isolating a potentially compromised device
* Safe Mode procedures
* Removing suspicious applications

### ₿ Cryptocurrency Recovery

`recv_cryp`

Provides guidance related to:

* Cryptocurrency incidents
* Wallet security
* Smart-contract approval revocation
* Wallet migration

---

# 2.2 Custom Entities

The agent uses **40 custom entities** to extract relevant variables from user messages.

| Category                  | Representative Entities                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Financial & Banking**   | `@bank_name`, `@crypto_coin`, `@payment_app`, `@financial_term`, `@credit_card_network`, `@remittance_service`                                                                                                                                                                                                                                                                                        |
| **Legal & Regulatory**    | `@government_agency`, `@tax_agency`, `@customs_agency`, `@id_document`                                                                                                                                                                                                                                                                                                                                |
| **Attack Vectors**        | `@malware_type`, `@phishing_term`, `@urgency_trigger`, `@extortion_term`, `@remote_desktop_app`, `@compromised_data_type`, `@two_factor_method`                                                                                                                                                                                                                                                       |
| **Ecosystem & Platforms** | `@job_portal`, `@ecommerce_site`, `@delivery_service`, `@device_type`, `@os_version`, `@browser_name`, `@telecom_provider`, `@loan_app`, `@investment_platform`, `@dating_app`, `@tech_support_company`, `@antivirus_brand`, `@lottery_name`, `@fake_charity`, `@booking_site`, `@airline_name`, `@hotel_chain`, `@real_estate_platform`, `@scam_category`, `@recovery_scam_term`, `@social_platform` |

---

# 🔌 3. Integration & Chatbot Architecture

## 3.1 How the Chatbot Works

The chatbot follows a multi-stage conversational pipeline:

```text
User Message
     │
     ▼
┌─────────────────────────────┐
│ Telegram / Web Demo         │
│ User Input                  │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ Google Dialogflow ES        │
│ NLP + Intent Classification │
│ + Entity Extraction         │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ Context Management           │
│ Recovery / Threat Flows      │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ Telegram Custom Payload     │
│ Markdown + Inline Buttons   │
└─────────────────────────────┘
```

### Processing Stages

**1. Input Ingestion**

The user submits:

* A suspicious message
* Email text
* A payment-related query
* A recovery request

The input can be submitted through Telegram or the configured Web Demo.

**2. NLP Classification**

Dialogflow processes the natural-language input and attempts to match it against the project's intent structure.

Custom entities extract relevant information from the message.

**3. Context Management**

Multi-step recovery workflows use Dialogflow input/output contexts:

```text
Input Context Lifespan: 2
Output Context Lifespan: 0
```

This helps isolate recovery interactions from general threat-detection intents.

**4. Response Dispatch**

Responses are delivered through Telegram custom payloads with:

* Markdown formatting
* Warning cards
* Recovery instructions
* Inline keyboards

---

# 🎛️ 4. Machine Learning Configuration

The project uses a Dialogflow classification threshold of:

```text
0.35
```

This threshold is configured to control intent-matching sensitivity and reduce unwanted intent overlap.

> **Important:** The `0.35` threshold is a configuration value. It should not be interpreted as a guaranteed `95%+` accuracy figure unless accuracy has been independently measured and documented using a defined test dataset.

---

# 🛠️ 5. Deployment Instructions

## Prerequisites

Before deploying ScamShield AI, install/configure:

* Python `3.13`
* Google Cloud Platform account
* Dialogflow ES API access
* Telegram Bot API credentials

---

## Step 1 — Clone the Repository

```bash
git clone https://github.com/YourUsername/IDAI101-2605192--Gaurav-Gautam-Bardia.git

cd IDAI101-2605192--Gaurav-Gautam-Bardia
```

---

## Step 2 — Generate the Agent Archive

Run:

```bash
python ScamShield_Engine_Fixed.py
```

The script generates:

```text
ScamShield-Production-Fixed.zip
```

The archive contains the Dialogflow configuration, including the project's intents, entities, and metadata.

---

## Step 3 — Import into Dialogflow ES

1. Open the [Dialogflow ES Console](https://dialogflow.cloud.google.com/).
2. Open the required Dialogflow agent.
3. Navigate to **Settings → Export and Import**.
4. Select **RESTORE FROM ZIP**.
5. Select:

```text
ScamShield-Production-Fixed.zip
```

6. Enter:

```text
RESTORE
```

7. Confirm the restoration.

---

## Step 4 — Train the Agent

Navigate to:

**ML Settings**

Confirm the classification threshold is configured as:

```text
0.35
```

Then select **TRAIN**.

---

## Step 5 — Enable Integrations

Open:

**Integrations → Telegram**

Then:

1. Connect the Telegram bot.
2. Provide the Bot API token generated through `@BotFather`.
3. Enable the Telegram integration.
4. Enable the Web Demo if configured.
5. Test the chatbot.

---

# 🧪 6. Testing & Optimization Results

The chatbot was evaluated using multiple scenarios covering legitimate messages, active fraud, impersonation, social engineering, and recovery workflows.

|  # | Test Scenario / Query                                                                           | Matched Intent                     | Result                                      |
| -: | ----------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------- |
|  1 | `"Rs 1,450.00 spent on your HDFC Bank Card ending 4082 at RELIANCE RETAIL..."`                  | `00_legitimate_communication`      | **PASS** — Identified as safe               |
|  2 | `"Notice from Cyber Crime Cell: Your ID is linked to money laundering under Digital Arrest..."` | `06_digital_arrest`                | **PASS** — High-severity alert triggered    |
|  3 | `"URGENT: Your electricity connection will be disconnected tonight at 9:30 PM..."`              | `29_utility_shutoff_impersonation` | **PASS** — Fake bill alert flagged          |
|  4 | `"Urgent wire transfer processed for consultant today from CEO office..."`                      | `54_social_engineering_isolation`  | **PASS** — Executive impersonation detected |
|  5 | User clicks `[⚠️ I'm Stuck]` during bank-card freezing                                          | `72_recovery_financial_stuck`      | **PASS** — Context-gated escalation routed  |

### Testing Areas

Testing focused on:

* Intent classification
* Entity extraction
* Legitimate-message filtering
* Scam detection
* Context handling
* Recovery-flow routing
* Telegram interactive responses

---

# 📂 7. Repository Structure

```text
IDAI101-2605192--Gaurav-Gautam-Bardia/
│
├── agent.json
│   └── Core Dialogflow agent configuration
│
├── package.json
│   └── Agent version and dependency metadata
│
├── ScamShield_Engine_Fixed.py
│   └── Python 3.13 master configuration generator
│
├── ScamShield-Production-Fixed.zip
│   └── Dialogflow production deployment archive
│
├── intents/
│   └── Dialogflow intent definitions and training phrases
│
├── entities/
│   └── Custom entity definitions and entry maps
│
├── assets/
│   └── Test screenshots and execution evidence
│
└── README.md
    └── Project documentation
```

---

# ⚖️ 8. Ethical AI & Privacy Standards

## 🔐 Zero Credential Harvesting

ScamShield AI is designed not to request, log, or store sensitive authentication credentials such as:

* Bank PINs
* Passwords
* OTPs
* Authentication codes

## 🧘 Calm De-escalation Design

The chatbot aims to avoid unnecessarily alarmist responses.

Instead, responses focus on:

1. Identifying potential risks
2. Explaining why a situation may be suspicious
3. Providing clear safety guidance
4. Offering structured recovery actions

This design is intended to help users respond rationally during high-pressure fraud situations.

---

# ⚠️ 9. Limitations

ScamShield AI is a conversational safety assistant and is not an infallible fraud-detection system.

Its output depends on:

* User-provided information
* Intent definitions
* Training phrases
* Entity configuration
* Context configuration
* Dialogflow classification

Users should independently verify suspicious communications through appropriate official channels.

---

# 📊 10. Project Summary

| Component                    | Implementation       |
| ---------------------------- | -------------------- |
| **AI Platform**              | Google Dialogflow ES |
| **Frontend Integration**     | Telegram Bot API     |
| **Programming Language**     | Python 3.13          |
| **Production Intents**       | 85                   |
| **Custom Entities**          | 40                   |
| **Recovery Pipelines**       | 5                    |
| **Classification Threshold** | `0.35`               |
| **Testing Scenarios**        | 5                    |
| **Deployment Status**        | Live                 |

---

# 👨‍💻 11. Student Information

**Gaurav Gautam Bardia**
Candidate Registration Number: `2605192`
Udgam School For Children

**CRS:** Artificial Intelligence
**Course:** Artificial Intelligence: Real-World Applications and Implications

---

# 📚 12. References

* [Google Dialogflow ES](https://dialogflow.cloud.google.com/)
* [Telegram Bot API](https://core.telegram.org/bots)
* [Python](https://www.python.org/)

---

## 🛡️ ScamShield AI

**An AI-powered conversational assistant for identifying, understanding, and responding to digital scam threats.**
