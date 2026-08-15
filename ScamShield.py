import os
import json
import uuid
import shutil

AGENT_NAME = "ScamShield"
INTENTS_DIR = os.path.join(AGENT_NAME, "intents")
ENTITIES_DIR = os.path.join(AGENT_NAME, "entities")

# --- 40 CYBERCRIME ENTITIES ---
ENTITIES = [
    "bank_name", "crypto_coin", "social_platform", "job_portal", "ecommerce_site",
    "payment_app", "delivery_service", "government_agency", "id_document", "malware_type",
    "phishing_term", "urgency_trigger", "financial_term", "scam_category", "device_type",
    "os_version", "browser_name", "telecom_provider", "loan_app", "investment_platform",
    "dating_app", "tech_support_company", "antivirus_brand", "tax_agency", "insurance_company",
    "credit_card_network", "gift_card_brand", "remittance_service", "customs_agency", "lottery_name",
    "extortion_term", "remote_desktop_app", "two_factor_method", "compromised_data_type", "recovery_scam_term",
    "fake_charity", "booking_site", "airline_name", "hotel_chain", "real_estate_platform"
]

# --- 55 DIRECT THREAT DETECTION PROFILES (01 TO 55) ---
THREAT_PROFILES = [
    ("bank_phishing", [
        "Dear customer your bank account has been locked due to incomplete pan verification",
        "Your bank account is suspended click here to update your KYC immediately",
        "Urgent bank notice your account will be blocked in 24 hours click link to verify",
        "State bank alert your netbanking password expired update via this portal",
        "Your debit card access has been restricted due to mandatory KYC compliance",
        "Dear Customer, Your SBI NetBanking account has been suspended today due to expired KYC",
        "Click http://sbi-kyc-verify-portal.in to submit PAN card and resume services immediately",
        "IT System Alert Your organizational account password will expire in 2 hours update at portal",
        "CRITICAL Password Expiration Notice for Corporate ID Keep Same Password Synchronize Account"
    ], "Phishing Alert: Never click SMS or email links for KYC or password updates. Legitimate organizations and banks do not suspend accounts via SMS links."),

    ("upi_fraud", [
        "You received a cashback of 1000 rupees open your UPI app and enter 6 digit pin",
        "Scan this QR code to claim your prize money directly in your bank account",
        "Enter your UPI PIN to approve your refund payment from merchant",
        "Receive 500 rupees instant bonus approve request on PhonePe",
        "Buyer sent a collect request claiming it will credit funds into your account"
    ], "UPI Fraud: Entering a UPI PIN always deducts money. You never need a PIN to receive funds."),

    ("credit_card_theft", [
        "Your credit card was charged 450 dollars at an unknown store click to dispute",
        "Unauthorized international transaction detected on your card freeze immediately",
        "Card blocking alert click link to confirm recent transaction",
        "Suspicious swipe of 25000 rupees detected on your Visa card dispute here",
        "Your credit card limit has been upgraded click to verify card details and CVV"
    ], "Card Theft: Immediately freeze your card via your banking app to prevent further unauthorized charges."),

    ("loan_app_extortion", [
        "Instant loan app threatening to send morphed photos to my contacts",
        "Pay high interest fee immediately or we will leak your personal gallery",
        "Harassing calls from illegal loan agent demanding fake service charges",
        "Loan recovery agent sent threats on WhatsApp with my private photo album",
        "Micro loan application demanding access to entire contact list and blackmailing"
    ], "Loan App Extortion: Uninstall the app, revoke permissions, and do not pay. Paying leads to more blackmail."),

    ("crypto_investment", [
        "Guaranteed 200 percent return in 24 hours join top crypto trading signal group",
        "Invest 100 dollars in bitcoin and get guaranteed daily profits",
        "Exclusive crypto arbitrage bot double your ethereum in three days",
        "Deposit USDT to our liquidity pool and receive 10 percent fixed daily dividend",
        "VIP crypto investment platform offering zero risk guaranteed margin trading"
    ], "Crypto Scam: Guaranteed high returns in crypto are always fraudulent. Block and report the group admins."),

    ("digital_arrest", [
        "Notice from Cyber Crime Cell Mumbai Your phone number has been linked to an illegal money laundering syndicate You are placed under Digital Arrest",
        "Notice from CBI Cyber Cell your mobile number is linked to money laundering",
        "You are under digital arrest do not disconnect this video call or leave your room",
        "Illegal narcotics found in your parcel stay on video call for live interrogation",
        "Supreme Court digital warrant issued against your identity stay on Skype",
        "Police officer on WhatsApp video call placing me under digital custody"
    ], "Digital Arrest: Police and courts do not conduct arrests, trials, or interrogations over Skype or WhatsApp."),

    ("police_impersonation", [
        "Traffic police officer demanding immediate fine payment via UPI or gift card",
        "Fake cop calling claiming my son was caught in a legal crime pay fine now",
        "Police officer threatening arrest warrant unless money is transferred immediately",
        "DCP Cyber Crime demanding settlement fee over phone to drop FIR",
        "Officer calling from police station asking for immediate online settlement"
    ], "Impersonation: Real police officers will never ask for UPI payments or online transfers to clear a warrant."),

    ("customs_clearance", [
        "Mumbai customs intercepted foreign gift parcel pay clearance tax to release",
        "Customs officer demanding clearance fee for expensive package sent by online friend",
        "Urgent parcel held at airport customs pay duty fee via random UPI link",
        "Foreign currency package held at Delhi airport pay anti money laundering clearance",
        "Online courier customs fee requested via personal bank account"
    ], "Customs Scam: Scammers claim a foreign friend sent a gift but you must pay clearance fees. Never pay."),

    ("tax_agency_fraud", [
        "Income Tax Department approved refund of 15000 rupees click link to claim",
        "Tax evasion notice pay immediate penalty fee to avoid legal prosecution",
        "Update your bank account details to process pending tax refund",
        "IRS final notice tax audit penalty required via immediate wire transfer",
        "Direct tax refund pending verify your credit card details to receive amount",
        "Tax Refund Notification Reference #ITR-2025-26/90182 Submit your active NetBanking credentials"
    ], "Tax Fraud: Tax departments process refunds directly to linked bank accounts, never via SMS or email links."),

    ("tech_support", [
        "Windows warning alert your computer is infected with critical spyware call support",
        "Microsoft tech support calling to fix remote security breach on your laptop",
        "Apple security popup lock your browser call fake toll free number",
        "Your firewall has been compromised call certified technician immediately",
        "System alert Trojan virus detected call Microsoft help desk to unlock PC"
    ], "Tech Support: Microsoft and Apple do not call you or display warning popups with phone numbers."),

    ("remote_access_takeover", [
        "Customer support asking me to install AnyDesk to solve banking app issue",
        "Download QuickSupport app to receive technical refund from support agent",
        "Remote desktop code requested by phone caller to verify account",
        "Support agent asking to open TeamViewer and provide 9 digit connection ID",
        "Caller instructed me to install screen sharing APK to complete KYC"
    ], "Remote Access: Never install AnyDesk or TeamViewer at the request of a caller. They will drain your bank accounts."),

    ("sim_swap", [
        "Mobile SIM lost network signal suddenly after receiving e-SIM upgrade text",
        "Telecom operator SMS asking to forward 20 digit SIM number for 5G upgrade",
        "Unauthorized SIM swap detected banking OTPs intercepted",
        "Airtel Jio SMS saying send 121 with SIM number to avoid disconnection",
        "Sudden No Service icon on phone after caller asked to confirm SIM verification"
    ], "SIM Swap: Your number was ported to a scammer. Contact your mobile operator immediately to block the SIM."),

    ("otp_bypass", [
        "Accidentally shared 6 digit verification OTP code with caller",
        "Caller asking for SMS verification code to cancel wrong transaction",
        "Please forward the text message you received to verify your delivery",
        "Bank representative asking for OTP to stop fraudulent transaction",
        "Shared authentication code for WhatsApp registration with unknown person"
    ], "OTP Fraud: Scammers use your OTP to authorize transactions. Never share 6-digit verification codes."),

    ("delivery_fee_scam", [
        "IndiaPost Your package IND-902-881 cannot be delivered due to missing house number Update your full address within 12 hours",
        "India Post Package delivery failed due to incorrect address pay redelivery charge",
        "Your parcel is held at customs warehouse click link to pay small clearance fee",
        "Delivery address incomplete update your details and pay shipping fee",
        "FedEx delivery attempt failed update zip code and pay 25 rupees re-dispatch fee",
        "Courier package suspended click postal link to verify delivery address",
        "parcel-redirection-fee update address to avoid return to sender"
    ], "Delivery Phishing Scam: Fake postal links steal credit card details by demanding a tiny 'redelivery' or 'address update' fee."),

    ("marketplace_buyer_fraud", [
        "OLX buyer sending QR code saying scan this to receive advance payment",
        "Buyer sent a money transfer link demanding my UPI PIN to accept deposit",
        "Marketplace buyer asking for bank details to send advance booking amount",
        "Buyer asking me to send 1 rupee to verify account before sending full payment",
        "Quikr buyer insisting on barcode scan to transfer product price"
    ], "Marketplace Fraud: A buyer sending a QR code is trying to pull money from your account. Scanning a QR code only sends money."),

    ("marketplace_seller_fraud", [
        "Army personnel selling cheap second hand vehicle demanding advance transport fee",
        "Seller asking for token amount before showing house or vehicle in person",
        "Fake online store offering 90 percent discount pay full amount before shipping",
        "Military officer posting discounted iPhone on OLX asking for gate pass clearance fee",
        "Used car seller refusing in-person inspection demanding courier charges upfront"
    ], "Seller Fraud: 'Army personnel' offering cheap vehicles with advance transport fees is a known scam."),

    ("romance_scam", [
        "Dating app match asking for money transfer for medical emergency or plane ticket",
        "Met online partner who claims to be stuck at airport needing urgent cash",
        "Online friend asking for loan after building trust for two weeks",
        "Tinder match claiming to be deployed abroad needing funds for leave clearance",
        "Romantic partner online asking to receive funds into my bank account"
    ], "Romance Scam: Scammers build emotional trust over weeks before asking for emergency or travel money."),

    ("pig_butchering", [
        "Dating app match convincing me to invest money on a special crypto platform",
        "Online friend giving inner market trading tips on a custom broker website",
        "High profit gold trading website recommended by online dating contact",
        "Met person on Hinge who taught me how to trade foreign exchange on unregulated broker",
        "Online romantic interest asking to deposit funds into private liquidity app"
    ], "Pig Butchering: A romance scam hybrid where the scammer manipulates you into a fake trading platform."),

    ("task_based_scam", [
        "Greetings from HR Global We have flexible part-time positions open Earn Rs 3500 Rs 8000 daily by rating Google Maps locations",
        "Earn 300 dollars a day by liking videos on YouTube contact HR bot on Telegram",
        "Part time work from home job like videos and submit screenshot for daily payout",
        "Pay small registration deposit to unlock high paying premium review tasks",
        "Hotel review rating task job on Telegram asking for prepaid recharge",
        "Earn 5000 daily by rating Google Maps locations join WhatsApp group"
    ], "Task Scam: They offer unrealistic pay for liking videos or rating maps, then demand prepaid deposits to unlock 'commissions'."),

    ("work_from_home_fraud", [
        "Data entry typing job paying 5000 rupees daily requires registration deposit fee",
        "Work from home form filling job demanding legal penalty for not completing quota",
        "Online typing job asking for security guarantee deposit money",
        "Legal notice sent via WhatsApp claiming breach of work from home contract pay fine",
        "Captcha solving job demanding advance software license purchase"
    ], "WFH Fraud: Offers promising thousands a day for basic typing are data harvesting and extortion traps."),

    ("lottery_prize", [
        "KBC lucky draw winner of 25 lakh rupees pay GST charge to receive check",
        "You won a luxury car in lucky contest pay registration processing fee",
        "Unclaimed lottery funds clear tax fee to release prize money",
        "WhatsApp lucky winner of 50 lakh rupees contact Rana Pratap Singh",
        "Shopping mall lucky coupon winner pay processing charges to dispatch gift"
    ], "Lottery Scam: You cannot win a lottery you did not enter. Never pay 'processing fees' for a prize."),

    ("fake_customer_care", [
        "Called customer care number found on Google search and agent asked for remote access",
        "Fake refund support line asking for card details to process refund",
        "Searched bank helpline on Google and caller asked for UPI PIN",
        "Zomato Swiggy fake customer support executive asking to install payment APK",
        "Gas agency helpline from search engine asked for debit card CVV"
    ], "Fake Support: Scammers manipulate Google search results to show their numbers for major brands. Use in-app support only."),

    ("gift_card_extortion", [
        "Boss sending urgent text asking to buy Apple iTunes gift cards for client",
        "Government agency demanding tax penalty payment using Steam gift cards",
        "Pay legal fine using Amazon gift card claim codes",
        "CEO urgent email asking to purchase Google Play gift cards and email scratch codes",
        "Immigration officer demanding clearance payment via Target gift vouchers"
    ], "Gift Card Scam: No legitimate business or government agency accepts iTunes or Amazon gift cards."),

    ("recovery_scam", [
        "Hacker on Instagram promising to recover lost crypto or money for upfront fee",
        "Cyber recovery agent claiming they can hack scammer account to return funds",
        "Unsolicited message offering guarantee fund retrieval for fee",
        "Private investigator claiming to retrieve scammed funds if I pay initial legal retainer",
        "Ethical hacker offering to recover stolen wallet funds for 10 percent deposit"
    ], "Recovery Scam: Scammers target victims again, promising to recover lost money for an upfront fee. Rely only on police."),

    ("ai_voice_cloning_grandparent", [
        "Grandma please help I got into a car accident in another city and police are holding me",
        "I need bail money right now send money via Zelle don't tell my parents",
        "Your grandson is in jail call from emergency bail lawyer need immediate transfer",
        "AI voice sounded exactly like my son crying saying he was kidnapped pay ransom",
        "Daughter's voice on phone crying asking to wire hospital funds urgently"
    ], "AI Voice Scam: Scammers clone voices of family members in distress. Always call back on a known personal number to verify."),

    ("deepfake_video_extortion", [
        "Extortionist threatening to leak AI generated explicit video of me to my contacts",
        "Deepfake nude photo blackmail pay bitcoin or photos will be sent to family",
        "Social media hacker created fake explicit video demanding ransom payment",
        "Received morphed AI video of my face attached to adult clip demanding money",
        "Blackmailer sent preview of deepfake explicit photo threatening social media blast"
    ], "Deepfake Extortion: Do not pay. Report the account, document the evidence, and file a cybercrime report immediately."),

    ("quishing_qr_code_fraud", [
        "Fake QR code sticker on public parking meter redirecting to phishing payment page",
        "Scanned QR menu in restaurant and it prompted to download suspicious APK",
        "Malicious QR code sticker overlay on public payment kiosk",
        "Scanned parking QR code and entered credit card on lookalike URL",
        "QR code flyer on car windshield demanding toll payment online"
    ], "Quishing (QR Scam): Fake QR stickers overlay real ones to redirect to phishing/malware. Check URLs before entering credentials."),

    ("e_sim_swapping_fraud", [
        "Received email stating eSIM transfer initiated on your mobile line click to cancel",
        "Cellular line lost signal after receiving QR code for free 5G eSIM activation",
        "Carrier alert unauthorized eSIM download detected on your account",
        "Scanned carrier QR code sent via email and lost cellular network connectivity",
        "eSIM activation barcode sent by SMS claiming mandatory carrier network update"
    ], "eSIM Hijacking: Contact your mobile carrier immediately if your line suddenly loses service or receives unauthorized transfer alerts."),

    ("utility_shutoff_impersonation", [
        "Electricity department warning power line will be disconnected in 30 minutes due to unpaid bill",
        "Urgent gas bill notice pay immediately via Zelle to avoid instant shutoff",
        "Water company threat demanding immediate payment via gift card",
        "Power board SMS pay last month pending bill on this 10 digit number to avoid blackout",
        "Electricity officer calling demanding immediate transfer before technician cuts wire",
        "URGENT Your electricity connection will be disconnected tonight at 930 PM because your previous month bill was not updated"
    ], "Utility Scam: Utility companies never demand immediate payment via personal phone numbers or third-party links under threat of instant shutoff."),

    ("toll_road_smishing", [
        "Toll Notice You have an unpaid toll fee of 4 dollars to avoid 50 dollar late fine pay now",
        "Final warning unpaid toll road fee click link to clear balance",
        "Toll services update unpaid balance on your vehicle click to pay",
        "SunPass EZPass overdue toll payment required immediately to avoid court summons",
        "Highway toll invoice unpaid vehicle registration will be suspended click link"
    ], "Toll Smishing: Fake SMS alerts claim unpaid toll fees with urgent penalty threats to steal card info. Use official toll portals only."),

    ("student_loan_forgiveness_scam", [
        "Government student loan forgiveness approval pay processing fee to clear debt",
        "Instant student debt relief program requires upfront administrative charge",
        "Call now to wipe out student loan balance for a small processing fee",
        "Federal student loan discharge pre-approved pay document preparation fee",
        "Debt relief counselor asking for direct monthly payments to erase college loan"
    ], "Loan Relief Scam: Official government student loan forgiveness programs never require upfront fees."),

    ("fake_job_interview_telegram", [
        "Recruiter offering high paying remote job with interview conducted entirely on Telegram text",
        "Company sending check to buy home office equipment and asking to wire back extra funds",
        "Pay for onboarding training software before starting remote job",
        "HR manager conducting interview via Wire chat offering 50 dollars an hour",
        "Received job offer without live video interview asked to pay background check fee"
    ], "Fake Remote Interview: Legitimate companies do not conduct entire interviews via text apps or send fake checks for equipment."),

    ("check_cashing_overpayment", [
        "Buyer sent cashier check for higher amount than item cost and asked to wire difference back",
        "Car wrap advertising company sent check to deposit and wire money to decal painter",
        "Deposited check bounced after I already wired back the extra funds",
        "Mystery shopper received advance cashier check asked to test wire transfer service",
        "Overpayment check received for marketplace item buyer demanding refund of excess"
    ], "Overpayment Scam: A deposited check can bounce weeks later. Never send money back from an unexpected check deposit."),

    ("crypto_drainer_airdrop", [
        "Connected crypto wallet to claim free NFT airdrop and all tokens were stolen",
        "Malicious smart contract request drained ethereum wallet balance",
        "Click link to claim free token voucher wallet drainer attack",
        "Signed permit transaction on unverified DEX and lost entire balance",
        "Claim free Uniswap airdrop link prompted wallet signature that drained coins"
    ], "Crypto Drainer: Connecting your wallet to unverified 'airdrop' sites gives malicious smart contracts full access to drain tokens."),

    ("fake_crypto_exchange_kyc", [
        "Binance security alert account suspended click link to verify identity and 2FA",
        "Coinbase withdrawal request from unknown device click to cancel",
        "Crypto wallet locked due to missing KYC documentation click link",
        "Kraken alert unauthorized login attempt verify credentials on mirror portal",
        "Metamask security warning sync your 12 word recovery seed phrase"
    ], "Fake Crypto Alert: Phishing sites mimic major exchanges to steal login seeds and 2FA codes. Bookmark official URLs."),

    ("brushing_scam_amazon", [
        "Receiving random unordered Amazon packages addressed to me without paying",
        "Seller using my address to post verified fake reviews on marketplace",
        "Unsolicited parcels arriving at doorstep from foreign address",
        "Received cheap jewelry in the mail that I never ordered from online store",
        "Random package delivered with QR code to scan for surprise gift"
    ], "Brushing Scam: Receiving unsolicited packages means a seller created a fake buyer profile using your address to generate fake positive reviews."),

    ("fake_concert_event_ticket", [
        "Bought sold out concert tickets from seller on Twitter who blocked me after Zelle transfer",
        "Fake ticket PDF sent after paying advance money via mobile wallet",
        "Unverified individual selling VIP tickets requesting friends and family payment",
        "Instagram seller offering discounted IPL match tickets disappeared after payment",
        "Purchased festival passes via direct bank transfer and tickets were invalid at gate"
    ], "Ticket Fraud: Buying tickets directly from individuals via social media with peer-to-peer payments offers zero buyer protection."),

    ("streaming_account_phishing", [
        "Netflix payment failed account will be closed in 24 hours click link to update billing",
        "Spotify subscription expired click link to retain monthly membership rate",
        "Streaming service account suspended due to invalid credit card details",
        "Disney Plus payment renewal rejected click here to enter new card number",
        "Prime Video membership on hold verify your billing details on this link",
        "Warning 98% of Storage Used Incoming messages blocked",
        "Your Cloud Drive has exceeded its storage allocation of 15 GB",
        "Upgrade to the 100 GB promotional tier for free portal-verify-storage-drive",
        "Mailbox storage full incoming messages placed on hold click to upgrade"
    ], "Account / Storage Phishing: Service providers do not block incoming emails or suspend drives via third-party link prompts. Manage storage only inside official account settings."),

    ("fake_charity_disaster_fund", [
        "Fake charity collecting crypto donations for earthquake disaster victims",
        "Unverified NGO sending emergency donation links via WhatsApp",
        "Scam website mimicking official Red Cross donation page",
        "Social media campaign asking for wire transfers to help flood victims",
        "Crowdfunding page using copied tragedy photos redirecting funds to personal wallet"
    ], "Disaster Charity Fraud: Verify charities on official portals before donating via crypto or peer-to-peer apps."),

    ("sextortion", [
        "Blackmailer claiming they recorded explicit video during video chat and threatening to send to contacts",
        "Email claiming your webcam was hacked and asking for bitcoin to delete video",
        "Threat to publish private social media chat screenshots unless ransom is paid",
        "Caller claiming to have Pegasus spyware footage of my screen asking for crypto",
        "Blackmail email displaying an old compromised password demanding 500 dollars in BTC"
    ], "Sextortion: Do not pay. Lock down all social media privacy settings and ignore the scammer."),

    ("fake_payment_screenshot", [
        "Customer showed me a GPay success screenshot but I did not receive an SMS from my bank",
        "Buyer on marketplace sent a payment confirmation image but balance hasn't updated",
        "Received a spoofed Paytm transfer receipt generated by a fake app",
        "Shopper showed successful UPI transaction screen but shop soundbox did not speak",
        "Customer insisted transaction was debited showing green tick receipt on phone"
    ], "Spoofed Payment Screen: Never trust a payment screenshot. Always verify the transaction directly in your banking app or soundbox."),

    ("pf_epfo_withdrawal_scam", [
        "Received an SMS claiming my PF balance is ready to withdraw click link to process",
        "Agent demanding upfront fee and OTP to fast track my EPFO claim",
        "Click here to link identity to PF account or your funds will be blocked",
        "EPFO officer calling asking for UAN login credentials to clear pension",
        "SMS claiming provident fund annual bonus approved click to credit"
    ], "PF Fraud: The EPFO never asks for your OTP or advance fees over phone calls or SMS. Process claims only via official government portals."),

    ("fake_airline_cancellation", [
        "Received email that my flight is cancelled and I must call a toll-free number for a refund",
        "Fake airline support agent asking for credit card details to process cancellation fee",
        "SMS claiming my boarding pass is invalid click link to generate a new one",
        "Found airline helpline on Google and caller demanded cancellation fee via UPI",
        "Fake Indigo customer care number asked for AnyDesk to issue ticket refund"
    ], "Airline Phishing: Scammers send fake cancellation notices to force you to call rogue call centers. Verify status directly on official airline apps."),

    ("mule_account_recruitment", [
        "Someone offered me a 10 percent commission just to receive money in my bank and forward it to crypto",
        "Online job asking to use my personal current account to process company transactions",
        "Stranger asked to borrow my UPI ID to receive a payment and give him cash",
        "Telegram channel offering weekly payout to rent out personal savings account",
        "Asked to transfer funds between unknown accounts to earn cash commission"
    ], "Money Mule Scam: You are being recruited to launder stolen funds. You will be held legally and criminally responsible by law enforcement."),

    ("matrimonial_fraud", [
        "NRI match from matrimonial site says he sent expensive jewelry but I have to pay customs clearance",
        "Online prospective bride asking for immediate cash transfer due to sudden family hospital bill",
        "Matrimonial contact demanding I pay for their flight ticket to meet me",
        "Prospective groom from matrimonial app claiming his wallet was stolen on business trip",
        "Match on Shaadi app asking to invest in his uncle's private trading company"
    ], "Matrimonial Fraud: Scammers build fake profiles to extract money under the guise of emergencies or held gifts."),

    ("credit_card_reward_points", [
        "SMS warning my credit card reward points are expiring today click here to redeem for cash",
        "Caller asking me to download an APK file to claim my accumulated bonus points",
        "Fill out this form with your CVV and expiry date to unlock your annual card benefits",
        "Convert your credit card reward points to 5000 rupees cash click portal link",
        "Bank points redemption portal asking for netbanking username and OTP"
    ], "Reward Point Scam: Banks do not send links or APKs to redeem points. Redeem points strictly through your authenticated banking app."),

    ("fake_visa_immigration", [
        "Agent on WhatsApp guaranteeing a Canadian work visa if I pay the processing fee via UPI",
        "Received an offer letter for a UK job but they require a security deposit for the permit",
        "Immigration consultant demanding payment before scheduling a fake embassy appointment",
        "Guaranteed Europe work permit payment demanded via cryptocurrency",
        "Foreign embassy job offer asking to transfer document verification charge"
    ], "Visa Fraud: Visas cannot be guaranteed by third-party agents, and embassies never request payments via UPI or personal accounts."),

    ("pan_aadhaar_linking_fraud", [
        "Urgent SMS your PAN card will be deactivated tomorrow if not linked click link",
        "Pay late fee of 1000 rupees to link identity documents on this alternative portal",
        "Caller claiming to be from income tax department asking for OTP to complete document linking",
        "Notice of penalty for unlinked PAN card click link to pay government fine",
        "Fake NSDL portal asking for credit card payment to update identity card"
    ], "Document Fraud: Link official identification documents strictly through the official incometax.gov.in portal. Ignore threatening SMS deadlines."),

    ("fake_gaming_esports_tournament", [
        "Discord server asking for entry fee via UPI to join a high prize pool BGMI tournament",
        "Paid registration for an unofficial esports custom room but the organizer blocked me",
        "Click link to claim free in-game diamonds and weapon skins by entering account password",
        "Free Fire tournament admin vanished after collecting team registration money",
        "Phishing login page offering free Valorant points and game passes"
    ], "Esports Scam: Fake organizers collect entry fees for phantom tournaments, or use phishing links to steal gaming accounts."),

    ("crypto_cloud_mining", [
        "Website promising 5 percent daily returns if I deposit USDT into their cloud mining contract",
        "App requires an initial deposit to unlock the mining rig and withdraw my profits",
        "Telegram admin offering a guaranteed return investment in a remote bitcoin mining farm",
        "Cloud hash rate rental platform freezing balance and demanding upgrade fee",
        "Deposit ethereum to activate daily passive mining returns"
    ], "Cloud Mining Fraud: Guaranteed daily crypto returns are mathematically impossible. These are Ponzi schemes designed to steal your deposit."),

    ("electricity_bill_whatsapp", [
        "Received a WhatsApp message from a personal mobile number saying my electricity will be cut at 9 PM",
        "Caller claiming my last month electricity bill was not updated and asking to pay via link",
        "Message says contact the electricity officer on this personal number immediately to avoid blackout",
        "Power department disconnection warning sent from generic Gmail address",
        "WhatsApp notice demanding immediate electricity bill clearing via personal UPI QR"
    ], "Power Disconnection Scam: Electricity boards do not send disconnection threats via WhatsApp from 10-digit personal mobile numbers."),

    ("free_wifi_hacking", [
        "Connected to an open public Wi-Fi network and immediately received an unauthorized login alert",
        "Prompted to install a security certificate just to use the free coffee shop internet",
        "Logged into my banking app on a public network and noticed strange transaction requests",
        "Rogue access point mimicking airport Wi-Fi redirecting to credential harvest page",
        "Free public internet requiring entry of email password and phone number"
    ], "Wi-Fi Interception: Public, unencrypted networks allow attackers to intercept traffic. Never access financial apps without a VPN."),

    ("fake_charity_crowdfunding", [
        "Received a viral WhatsApp forward with a sick child's photo asking to donate to a personal UPI number",
        "Facebook ad for an animal shelter demanding immediate crypto donations to prevent closure",
        "Unverified crowdfunding link claiming to raise funds for disaster victims using generic photos",
        "Emotional video appeal on Instagram asking to transfer charity funds to a personal account",
        "Cancer treatment appeal using stolen hospital pictures redirecting to private UPI ID"
    ], "Crowdfunding Scam: Scammers steal tragic images from the internet to solicit funds. Only donate to registered, audited NGOs."),

    ("social_engineering_isolation", [
        "The caller insisted I must not hang up or tell my family members about this secret investigation",
        "Agent demanded I step out of the house and isolate myself before transferring the funds",
        "Threatened with a gag order claiming I would be arrested if I discussed the call with a lawyer",
        "Caller forbade me from disconnecting the line while walking to the bank ATM",
        "Told that informing anyone about the ongoing cyber audit will result in immediate imprisonment",
        "Urgent Availability Vendor Wire CEO office urgent wire transfer processed for our external consultant today Reply immediately"
    ], "Social Engineering / CEO Fraud: Scammers use executive impersonation and urgency to force wire transfers. Always verify out-of-band via phone before transferring funds."),

    ("fake_courier_drugs_extortion", [
        "FedEx automated call stating a package in my name was seized with illegal passports and drugs",
        "Courier agent transferred my call directly to a fake narcotics officer demanding a settlement fee",
        "Received a tracking link claiming my international shipment is under police investigation",
        "Customs courier alert stating illegal contraband was shipped using my identity card",
        "BlueDart IVR message saying parcel returned due to illegal items pay clearance"
    ], "Courier Extortion: Real courier companies do not transfer your call to police or cyber cells. This is a setup for a digital arrest scam.")
]

# --- 15 SCAM EDUCATION & EARLY SIGNS PROFILES (56 TO 70) ---
EDUCATION_PROFILES = [
    ("edu_universal_red_flags", ["What are the common signs of a scam?", "How do I know if I am being scammed?", "What are the universal red flags of cyber fraud?", "How to identify if someone is trying to scam me?", "Tell me the warning signs of all online scams"], "💡 *Universal Scam Red Flags:*\nNearly all scams share 4 patterns:\n1. *Artificial Urgency* (Do this in 10 mins or get arrested/blocked)\n2. *Forced Isolation* (Do not tell family or bank staff)\n3. *Odd Payments* (Demanding gift cards, crypto, or personal UPI)\n4. *Credential Harvest* (Asking for OTP, PIN, or Screen Share)"),
    ("edu_phishing_link_signs", ["How to spot a fake or phishing link?", "What are the signs of a fake website URL?", "How do I know if a bank link is fraudulent?", "Warning signs of a fake email or SMS link", "How can I tell if a website is real or fake?"], "💡 *Phishing Link Indicators:*\n• Lookalike domain names (e.g., `sbi-kyc-update.net` instead of `onlinesbi.sbi`)\n• Use of free subdomains or raw IP addresses\n• Generic greetings ('Dear Customer') without your real name\n• Poor spelling, grammatical errors, and extreme urgency threats"),
    ("edu_job_task_scam_signs", ["How to identify a fake job or task scam?", "What are the warning signs of employment fraud?", "How to know if a remote work offer is fake?", "Early signs of YouTube like and review scams", "How do Telegram work from home scams work?"], "💡 *Fake Job & Task Red Flags:*\n• Offers paying hundreds of dollars daily just to like videos, rate hotels, or write fake reviews\n• Recruitment and interviews conducted solely over Telegram/WhatsApp text\n• Requiring you to pay a 'security deposit' or 'recharge' to unlock premium tasks"),
    ("edu_romance_matrimonial_signs", ["How to spot a romance or matrimonial scammer?", "Warning signs of online dating scams", "How do I know if my online date is a catfish?", "Red flags in matrimonial profiles on Shaadi", "Signs that an online partner is manipulating me for money"], "💡 *Romance & Matrimonial Red Flags:*\n• Professes intense love or marriage commitment within days\n• Always makes excuses to avoid live video calls or in-person meetings\n• Claims to be an NRI, doctor, or military officer deployed abroad\n• Inevitably asks for money for a sudden medical crisis, lost passport, or customs clearance fee"),
    ("edu_crypto_investment_signs", ["How to spot fake cryptocurrency investment schemes?", "What are the signs of a crypto trading scam?", "How do I know if a crypto broker platform is fake?", "Early warning signs of crypto Ponzi schemes", "How to identify fraudulent crypto trading groups?"], "💡 *Crypto Investment Red Flags:*\n• Guaranteed daily or weekly profit promises (e.g., 'Double your money in 48 hours')\n• Unregulated trading platforms that allow easy deposits but freeze all withdrawals\n• Strangers on social media giving 'insider tips' or automated trading bot links"),
    ("edu_tech_support_popup_signs", ["How to know if a computer virus alert is fake?", "Signs of fake Microsoft tech support scams", "What are the red flags of tech support calls?", "How to spot fake Apple security warnings?", "Warning signs of remote desktop software fraud"], "💡 *Fake Tech Support Red Flags:*\n• Fullscreen browser pop-ups that lock your screen and display a toll-free number\n• Unsolicited phone callers claiming your router, computer, or identity has been hacked\n• Demanding you install AnyDesk, TeamViewer, or UltraViewer to fix the issue"),
    ("edu_predatory_loan_app_signs", ["How to spot illegal and blackmail loan apps?", "Warning signs of fake instant loan applications", "How do predatory micro-loan apps trap users?", "Signs a loan app is going to harass my contacts", "How to check if a mobile loan app is RBI approved?"], "💡 *Predatory Loan App Red Flags:*\n• Distributed via direct APK links or shady websites rather than verified app stores\n• Demands invasive permissions (Access to Full Contacts, Photo Gallery, Call Logs)\n• Deducts 40-50% upfront as 'processing fees' and gives an impossible 7-day repayment period\n• Uses morphed photos to harass and extort your friends and family"),
    ("edu_digital_arrest_police_signs", ["How to identify a fake digital arrest scam?", "What are the signs of fake CBI or police video calls?", "Can police arrest someone over WhatsApp video call?", "Warning signs of fake courier narcotics investigation", "How to know if a police arrest warrant on phone is real?"], "💡 *Digital Arrest Fraud Indicators:*\n• Law enforcement officers interrogating you over Skype or WhatsApp video calls\n• Showing fake ID cards, FIR documents, and Supreme Court letters with generic stamps\n• Placing you under 'Digital Custody' and demanding you stay on camera without contacting family\n• Demanding you transfer funds to a 'Government Safe Account' for verification"),
    ("edu_delivery_parcel_scam_signs", ["How to identify fake postal delivery text messages?", "What are the early signs of courier redelivery fraud?", "How do I know if an India Post delivery alert is fake?", "Warning signs of FedEx and BlueDart SMS scams", "How to spot fake shipping address update links?"], "💡 *Delivery & Postal Scam Signs:*\n• SMS sent from random 10-digit mobile numbers instead of registered courier sender IDs\n• Claims package cannot be delivered due to missing house number or incorrect zip code\n• Demands a tiny fee (e.g., ₹25 or $3) via an embedded link to steal credit/debit card numbers"),
    ("edu_marketplace_buyer_qr_signs", ["How to spot an OLX or marketplace buyer scam?", "Why does a buyer send a QR code to pay me?", "Warning signs of fake buyers on classifieds", "Early signs of marketplace advance payment fraud", "How do scammers trick sellers on OLX and Facebook?"], "💡 *Marketplace Buyer Fraud Signs:*\n• Buyer agrees to buy immediately without negotiating price or inspecting item\n• Buyer sends a QR code or payment link claiming 'Scan this to receive money'\n• Demands you enter your UPI PIN to approve receipt of funds (PIN is ONLY used to send money)"),
    ("edu_fake_customer_care_signs", ["How to spot fake customer care numbers on Google?", "Why are customer service numbers on search engines dangerous?", "Warning signs of fraudulent support executives", "How to verify if a helpline number is authentic?", "Signs that a customer care executive is a scammer"], "💡 *Fake Helpline Red Flags:*\n• Helpline numbers sourced from Google Search, Google Maps, or social media comments\n• Support agent asks you to download AnyDesk or QuickSupport to initiate a refund\n• Agent asks for your UPI PIN, debit card CVV, or banking OTP to resolve a complaint"),
    ("edu_lottery_giveaway_signs", ["How to know if a lottery or prize notification is fake?", "Warning signs of KBC lucky draw scams", "How to identify fraudulent online giveaways?", "Signs of fake contest winning letters", "How do I verify if a prize reward is real?"], "💡 *Lottery & Giveaway Red Flags:*\n• Winning a contest, lucky draw, or car you never registered for or bought tickets to\n• Congratulatory letters with fake logos of KBC, Tata, or international lottery boards\n• Demands for upfront 'GST', 'customs duty', or 'processing fees' before dispatching prize"),
    ("edu_ai_voice_deepfake_signs", ["How to detect an AI cloned voice scam call?", "What are the warning signs of deepfake video extortion?", "How do scammers use AI voice cloning to trick parents?", "Early signs of emergency kidnap voice scams", "How to verify if a distress call from family is real?"], "💡 *AI Voice & Deepfake Red Flags:*\n• A family member calls crying in distress claiming an accident, arrest, or kidnapping\n• Audio may sound slightly robotic, have unnatural breathing pauses, or sudden background cuts\n• Caller insists you must wire money instantly and forbids you from calling other relatives"),
    ("edu_utility_bill_threat_signs", ["How to spot fake electricity bill disconnection messages?", "Warning signs of power bill WhatsApp scams", "How do I know if an electricity board SMS is fake?", "Signs of fake water or gas bill payment demands", "Why do scammers send power cut notices at night?"], "💡 *Utility Bill Scam Indicators:*\n• Message sent via WhatsApp or personal mobile claiming electricity will be disconnected tonight\n• Contains an unknown 10-digit personal phone number to contact the 'officer'\n• Official utility boards never send disconnection threats with personal mobile numbers or QR codes"),
    ("edu_money_mule_signs", ["What are the warning signs of money mule recruitment?", "How to know if a job offer is actually money laundering?", "Signs that someone is using my bank account for illegal money", "Why is someone asking to borrow my UPI account?", "How to spot commission based fund transfer scams?"], "💡 *Money Mule Red Flags:*\n• Offers paying generous commissions just to receive bank transfers and forward funds to crypto/UPI\n• Strangers asking to 'rent' your bank account or borrow your payment QR code\n• Warning: Acting as a money mule makes you a legal co-conspirator in cyber crime under criminal law")
]

# --- 15 POST-SCAM RECOVERY PLAYBOOKS (71 TO 85) ---
PLAYBOOKS = [
    ("recovery_financial_start", "recv_fin", True, ["block card", "freeze account", "financial recovery", "how to block upi", "stop bank transaction", "help I was scammed of money", "money debited from bank"], "Step 1: Open your mobile banking app immediately and toggle 'Freeze Card' or 'Disable Online/International Transactions'. Do not wait for customer service if you can do it via the app.", [("✅ Done", "financial done"), ("⚠️ I'm Stuck", "financial stuck")]),
    ("recovery_financial_stuck", "recv_fin", False, ["financial stuck", "app not working", "bank closed", "can't log in", "no response from bank", "card freeze failed"], "Escalation: If the app fails, call the 24/7 emergency fraud number printed on the back of your debit/credit card. Do NOT search Google for bank helplines.", [("✅ Done", "financial done")]),
    ("recovery_financial_step2", "recv_fin", False, ["financial done", "card blocked", "done with step 1", "what next for bank", "card is frozen"], "Step 2: Note the unauthorized transaction amounts and exact timestamps. You must submit this data to your bank's official fraud dispute department within 3 days to limit liability.", [("📞 Report to 1930", "report 1930")]),
    ("recovery_police_start", "recv_pol", True, ["report 1930", "file fir", "police recovery", "how to call 1930", "report to cyber cell", "how to report to police", "file cyber complaint"], "Step 1: Dial 1930 immediately (National Cybercrime Helpline). Keep your bank transaction ID, timestamp, and the scammer's phone number/UPI ID ready.", [("✅ Done", "police done"), ("⚠️ I'm Stuck", "police stuck")]),
    ("recovery_police_stuck", "recv_pol", False, ["police stuck", "line busy", "1930 not connecting", "call dropping", "no one answering 1930"], "Escalation: If the 1930 phone hotline is busy, immediately file your financial fraud complaint online at cybercrime.gov.in.", [("✅ Done", "police done")]),
    ("recovery_police_step2", "recv_pol", False, ["police done", "reported to cybercrime", "done filing fir", "got acknowledgment number"], "Step 2: Save the 14-digit cybercrime acknowledgment number. Submit this acknowledgment directly to your bank manager to initiate the inter-bank fund freeze.", []),
    ("recovery_identity_start", "recv_id", True, ["change passwords", "lock accounts", "identity recovery", "hacked account", "secure my email", "someone hacked my whatsapp", "social media compromised"], "Step 1: Log into your primary email and social media accounts. Change passwords immediately and enable Time-Based Two-Factor Authentication (e.g., Google Authenticator).", [("✅ Done", "identity done"), ("⚠️ I'm Stuck", "identity stuck")]),
    ("recovery_identity_stuck", "recv_id", False, ["identity stuck", "forgot password", "no otp coming", "hacker changed password", "can't log in to email"], "Escalation: Use the official 'Account Recovery' page on a trusted device you previously used. Check your email settings to ensure the hacker didn't set up auto-forwarding rules.", [("✅ Done", "identity done")]),
    ("recovery_identity_step2", "recv_id", False, ["identity done", "passwords changed", "2fa enabled", "what next for accounts"], "Step 2: Navigate to your account's 'Security' or 'Active Sessions' tab. Force a logout on all unrecognized devices instantly.", []),
    ("recovery_device_start", "recv_dev", True, ["uninstall app", "scan pc", "device recovery", "remove anydesk", "close browser popup", "installed malicious apk", "screen sharing app installed"], "Step 1: Turn on Airplane Mode immediately to sever the attacker's connection. Once offline, delete the suspicious APK, AnyDesk, or screen-sharing application.", [("✅ Done", "device done"), ("⚠️ I'm Stuck", "device stuck")]),
    ("recovery_device_stuck", "recv_dev", False, ["device stuck", "can't uninstall", "screen is locked", "app won't delete", "admin privileges blocking"], "Escalation: Hard reboot your phone into 'Safe Mode' (holding power button and long-pressing 'Power Off'). This disables the malicious overlay so you can delete the app.", [("✅ Done", "device done")]),
    ("recovery_device_step2", "recv_dev", False, ["device done", "uninstalled suspicious app", "removed anydesk", "what next for phone"], "Step 2: Reconnect to the internet and run a full system scan using Google Play Protect or a verified anti-malware tool. Check your battery usage for hidden background processes.", []),
    ("recovery_crypto_start", "recv_cryp", True, ["revoke approvals", "disconnect wallet", "crypto recovery", "stop smart contract", "crypto drainer", "wallet drained", "signed phishing transaction"], "Step 1: Use Revoke.cash or a similar authorization tool to immediately revoke infinite approvals given to the malicious smart contract. Transfer remaining funds to a hardware wallet.", [("✅ Done", "crypto done"), ("⚠️ I'm Stuck", "crypto stuck")]),
    ("recovery_crypto_stuck", "recv_cryp", False, ["crypto stuck", "no gas fee", "wallet frozen", "transaction failing", "insufficient eth to revoke"], "Escalation: You need network gas to execute a revoke transaction. Quickly transfer a tiny amount of ETH/BNB from a centralized exchange to cover the fee and push the revoke through.", [("✅ Done", "crypto done")]),
    ("recovery_crypto_step2", "recv_cryp", False, ["crypto done", "revoked contract approvals", "transferred remaining crypto", "what next for wallet"], "Step 2: Abandon that compromised wallet permanently. Never reuse a compromised seed phrase or private key. Generate a completely new wallet from scratch.", [])
]

# --- DIRECTORY CLEANUP & INITIALIZATION ---
if os.path.exists(AGENT_NAME):
    shutil.rmtree(AGENT_NAME)
os.makedirs(INTENTS_DIR)
os.makedirs(ENTITIES_DIR)

# --- AGENT METADATA SCHEMA ---
agent_json = {
    "description": "ScamShield Production Environment - 85 Intents",
    "language": "en",
    "shortDescription": "",
    "examples": "",
    "linkToDocs": "",
    "displayName": "ScamShield",
    "disableInteractionLogs": False,
    "disableViberInteractionLogs": False,
    "defaultTimezone": "Asia/Kolkata",
    "isPrivate": True,
    "mlMinMatchP": 0.35,
    "supportedLanguages": [],
    "enableOneClickIntegration": False,
    "oneClickIntegration": None,
    "webhook": {"url": "", "username": "", "headers": {}, "available": False, "useForDomains": False, "cloudFunctionsEnabled": False, "cloudFunctionsInitialized": False},
    "chatBubbleApiInfo": {"useForDomains": False},
    "isDeviceAgent": False,
    "analyzeQueryTextSentiment": False,
    "enabledKnowledgeBaseNames": [],
    "knowledgeServiceConfidenceAdjustment": 0.0,
    "dialogBuilderMode": False,
    "baseActionPackagesUrl": "",
    "enableSpellCorrection": False
}
with open(os.path.join(AGENT_NAME, "package.json"), "w") as f:
    json.dump({"version": "1.0.0"}, f)
with open(os.path.join(AGENT_NAME, "agent.json"), "w") as f:
    json.dump(agent_json, f, indent=2)

# --- ENTITIES ---
for entity in ENTITIES:
    e_meta = {
        "id": str(uuid.uuid4()), "name": entity, "isOverridable": True,
        "isEnum": False, "isRegexp": False, "automatedExpansion": True, "allowFuzzyExtraction": True
    }
    with open(os.path.join(ENTITIES_DIR, f"{entity}.json"), "w") as f:
        json.dump(e_meta, f, indent=2)
    entries = [{"value": entity, "synonyms": [entity, f"fake_{entity}", f"scam_{entity}"]}]
    with open(os.path.join(ENTITIES_DIR, f"{entity}_entries_en.json"), "w") as f:
        json.dump(entries, f, indent=2)

# --- BUILD INTENT FUNCTION (STRICT SINGLE PAYLOAD) ---
def build_intent(intent_name, input_ctx, output_ctx, phrases, text, buttons=[]):
    intent_id = str(uuid.uuid4())
    clean_text = text.replace("*", "")
    
    reply_markup = {}
    if buttons:
        reply_markup = {"inline_keyboard": [[{"text": btn_text, "callback_data": btn_cb}] for btn_text, btn_cb in buttons]}
    
    telegram_payload = {"text": text, "parse_mode": "Markdown"}
    if reply_markup:
        telegram_payload["reply_markup"] = reply_markup

    meta = {
        "id": intent_id,
        "name": intent_name,
        "auto": True,
        "contexts": input_ctx,
        "responses": [
            {
                "resetContexts": False,
                "affectedContexts": output_ctx,
                "parameters": [],
                "messages": [
                    {
                        "type": 0,
                        "lang": "en",
                        "speech": [clean_text]
                    },
                    {
                        "type": 4,
                        "lang": "en",
                        "payload": {"telegram": telegram_payload}
                    }
                ],
                "defaultResponsePlatforms": {},
                "speech": []
            }
        ],
        "priority": 500000,
        "webhookUsed": False,
        "webhookForSlotFilling": False,
        "fallbackIntent": False,
        "events": []
    }
    with open(os.path.join(INTENTS_DIR, f"{intent_name}.json"), "w") as f:
        json.dump(meta, f, indent=2)
    usersays = [{"id": str(uuid.uuid4()), "data": [{"text": p, "userDefined": False}], "isTemplate": False, "count": 0, "lang": "en", "updated": 0} for p in phrases]
    with open(os.path.join(INTENTS_DIR, f"{intent_name}_usersays_en.json"), "w") as f:
        json.dump(usersays, f, indent=2)

# --- 1. SYSTEM INTENTS ---
def create_system_intents():
    w_meta = {
        "id": str(uuid.uuid4()), "name": "Default Welcome Intent", "auto": True, "contexts": [],
        "responses": [{
            "resetContexts": False, "affectedContexts": [], "parameters": [],
            "messages": [
                {"type": 0, "lang": "en", "speech": ["Hello! I am ScamShield AI. Describe any suspicious message, call, or email to analyze."]},
                {"type": 4, "lang": "en", "payload": {"telegram": {"text": "🛡️ *Welcome to ScamShield AI*\n\nSend me any suspicious message, call transcript, or email to analyze, or ask about warning signs and emergency recovery steps.", "parse_mode": "Markdown"}}}
            ],
            "defaultResponsePlatforms": {}, "speech": []
        }],
        "priority": 500000, "webhookUsed": False, "webhookForSlotFilling": False,
        "fallbackIntent": False, "events": [{"name": "WELCOME"}],
        "conditionalResponses": [], "condition": "", "conditionalFollowupEvents": []
    }
    with open(os.path.join(INTENTS_DIR, "Default Welcome Intent.json"), "w") as f:
        json.dump(w_meta, f, indent=2)
    
    w_usersays = [{"id": str(uuid.uuid4()), "data": [{"text": p, "userDefined": False}], "isTemplate": False, "count": 0, "lang": "en", "updated": 0} 
                  for p in ["hi", "hello", "hey", "start", "good morning", "good evening", "help"]]
    with open(os.path.join(INTENTS_DIR, "Default Welcome Intent_usersays_en.json"), "w") as f:
        json.dump(w_usersays, f, indent=2)

    f_meta = {
        "id": str(uuid.uuid4()), "name": "Default Fallback Intent", "auto": True, "contexts": [],
        "responses": [{
            "resetContexts": False, "affectedContexts": [], "parameters": [],
            "messages": [
                {"type": 0, "lang": "en", "speech": ["I could not identify that scam pattern. Please describe the specific suspicious text, call demand, or link in detail."]},
                {"type": 4, "lang": "en", "payload": {"telegram": {"text": "I() could not identify that scam pattern. Please describe the specific suspicious text, call demand, or link in detail.", "parse_mode": "Markdown"}}}
            ],
            "defaultResponsePlatforms": {}, "speech": []
        }],
        "priority": 500000, "webhookUsed": False, "webhookForSlotFilling": False,
        "fallbackIntent": True, "events": [],
        "conditionalResponses": [], "condition": "", "conditionalFollowupEvents": []
        }
    with open(os.path.join(INTENTS_DIR, "Default Fallback Intent.json"), "w") as f:
        json.dump(f_meta, f, indent=2)

create_system_intents()

# --- 2. LEGITIMATE COMMUNICATION DETECTION INTENT (PREVENTS FALSE POSITIVES) ---
LEGITIMATE_PHRASES = [
    "spent on your HDFC Bank Card ending 4082 on 15-AUG-26 at RELIANCE RETAIL",
    "spent on your Bank Card ending at RELIANCE RETAIL Avl Bal If not done by you",
    "Your Amazon in order has shipped",
    "Your package containing Logitech Wireless Mouse is on its way",
    "Estimated Delivery Courier ATS Tracking You can track your package directly through the Amazon app",
    "Your OTP for login is Do not share this OTP with anyone",
    "Salary credited to your account ending"
]
build_intent("00_legitimate_communication", [], [], LEGITIMATE_PHRASES, "✅ *Legitimate Communication Detected:*\n\nThis message matches authentic transactional and shipping notification formats. Standard safety rule: Never share OTPs or login passwords with anyone calling you.")

# --- 3. GENERATE 01-55: THREAT DETECTION ---
for idx, (name, phrases, resp) in enumerate(THREAT_PROFILES, start=1):
    build_intent(f"{str(idx).zfill(2)}_{name}", [], [], phrases, f"⚠️ *Scam Detection Alert:*\n\n{resp}")

# --- 2. GENERATE 56-70: EDUCATION & EARLY SIGNS ---
for idx, (name, phrases, resp) in enumerate(EDUCATION_PROFILES, start=56):
    build_intent(f"{str(idx).zfill(2)}_{name}", [], [], phrases, f"{resp}")

# --- 3. GENERATE 71-85: RECOVERY PLAYBOOKS ---
for idx, (name, ctx, is_base, phrases, resp, buttons) in enumerate(PLAYBOOKS, start=71):
    in_ctx = [] if is_base else [ctx]
    out_ctx = [{"name": ctx, "lifespan": 2, "parameters": {}}] if not name.endswith("_step2") else [{"name": ctx, "lifespan": 0, "parameters": {}}]
    build_intent(f"{str(idx).zfill(2)}_{name}", in_ctx, out_ctx, phrases, f"🚨 *Emergency Protocol:*\n\n{resp}", buttons)

# --- PACKAGE MASTER ZIP ARCHIVE ---
shutil.make_archive(AGENT_NAME, 'zip', AGENT_NAME)
shutil.rmtree(AGENT_NAME)
print(f"SUCCESS: Generated {AGENT_NAME}.zip containing 85 Intents, 40 Entities, and dual-channel response support.")