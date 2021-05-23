import logging, requests, re
import inline_district_keyboard as idk
from cowin_api import CoWinAPI

from telegram import Sticker, BotCommand, Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters

def get_district_1() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Nicobar', callback_data='Nicobar-3'),
            InlineKeyboardButton('North and Middle Andaman', callback_data='North and Middle Andaman-1'),
        ],
        [
            InlineKeyboardButton('South Andaman', callback_data='South Andaman-2'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_2() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Anantapur', callback_data='Anantapur-9'),
            InlineKeyboardButton('Chittoor', callback_data='Chittoor-10'),
        ],
        [
            InlineKeyboardButton('East Godavari', callback_data='East Godavari-11'),
            InlineKeyboardButton('Guntur', callback_data='Guntur-5'),
        ],
        [
            InlineKeyboardButton('Krishna', callback_data='Krishna-4'),
            InlineKeyboardButton('Kurnool', callback_data='Kurnool-7'),
        ],
        [
            InlineKeyboardButton('Prakasam', callback_data='Prakasam-12'),
            InlineKeyboardButton('Sri Potti Sriramulu Nellore', callback_data='Sri Potti Sriramulu Nellore-13'),
        ],
        [
            InlineKeyboardButton('Srikakulam', callback_data='Srikakulam-14'),
            InlineKeyboardButton('Visakhapatnam', callback_data='Visakhapatnam-8'),
        ],
        [
            InlineKeyboardButton('Vizianagaram', callback_data='Vizianagaram-15'),
            InlineKeyboardButton('West Godavari', callback_data='West Godavari-16'),
        ],
        [
            InlineKeyboardButton('YSR District, Kadapa (Cuddapah)', callback_data='YSR District, Kadapa (Cuddapah)-6'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_3() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Anjaw', callback_data='Anjaw-22'),
            InlineKeyboardButton('Changlang', callback_data='Changlang-20'),
        ],
        [
            InlineKeyboardButton('Dibang Valley', callback_data='Dibang Valley-25'),
            InlineKeyboardButton('East Kameng', callback_data='East Kameng-23'),
        ],
        [
            InlineKeyboardButton('East Siang', callback_data='East Siang-42'),
            InlineKeyboardButton('Itanagar Capital Complex', callback_data='Itanagar Capital Complex-17'),
        ],
        [
            InlineKeyboardButton('Kamle', callback_data='Kamle-24'),
            InlineKeyboardButton('Kra Daadi', callback_data='Kra Daadi-27'),
        ],
        [
            InlineKeyboardButton('Kurung Kumey', callback_data='Kurung Kumey-21'),
            InlineKeyboardButton('Lepa Rada', callback_data='Lepa Rada-33'),
        ],
        [
            InlineKeyboardButton('Lohit', callback_data='Lohit-29'),
            InlineKeyboardButton('Longding', callback_data='Longding-40'),
        ],
        [
            InlineKeyboardButton('Lower Dibang Valley', callback_data='Lower Dibang Valley-31'),
            InlineKeyboardButton('Lower Siang', callback_data='Lower Siang-18'),
        ],
        [
            InlineKeyboardButton('Lower Subansiri', callback_data='Lower Subansiri-32'),
            InlineKeyboardButton('Namsai', callback_data='Namsai-36'),
        ],
        [
            InlineKeyboardButton('Pakke Kessang', callback_data='Pakke Kessang-19'),
            InlineKeyboardButton('Papum Pare', callback_data='Papum Pare-39'),
        ],
        [
            InlineKeyboardButton('Shi Yomi', callback_data='Shi Yomi-35'),
            InlineKeyboardButton('Siang', callback_data='Siang-37'),
        ],
        [
            InlineKeyboardButton('Tawang', callback_data='Tawang-30'),
            InlineKeyboardButton('Tirap', callback_data='Tirap-26'),
        ],
        [
            InlineKeyboardButton('Upper Siang', callback_data='Upper Siang-34'),
            InlineKeyboardButton('Upper Subansiri', callback_data='Upper Subansiri-41'),
        ],
        [
            InlineKeyboardButton('West Kameng', callback_data='West Kameng-28'),
            InlineKeyboardButton('West Siang', callback_data='West Siang-38'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_district_4() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Baksa', callback_data='Baksa-46'),
            InlineKeyboardButton('Barpeta', callback_data='Barpeta-47'),
        ],
        [
            InlineKeyboardButton('Biswanath', callback_data='Biswanath-765'),
            InlineKeyboardButton('Bongaigaon', callback_data='Bongaigaon-57'),
        ],
        [
            InlineKeyboardButton('Cachar', callback_data='Cachar-66'),
            InlineKeyboardButton('Charaideo', callback_data='Charaideo-766'),
        ],
        [
            InlineKeyboardButton('Chirang', callback_data='Chirang-58'),
            InlineKeyboardButton('Darrang', callback_data='Darrang-48'),
        ],
        [
            InlineKeyboardButton('Dhemaji', callback_data='Dhemaji-62'),
            InlineKeyboardButton('Dhubri', callback_data='Dhubri-59'),
        ],
        [
            InlineKeyboardButton('Dibrugarh', callback_data='Dibrugarh-43'),
            InlineKeyboardButton('Dima Hasao', callback_data='Dima Hasao-67'),
        ],
        [
            InlineKeyboardButton('Goalpara', callback_data='Goalpara-60'),
            InlineKeyboardButton('Golaghat', callback_data='Golaghat-53'),
        ],
        [
            InlineKeyboardButton('Hailakandi', callback_data='Hailakandi-68'),
            InlineKeyboardButton('Hojai', callback_data='Hojai-764'),
        ],
        [
            InlineKeyboardButton('Jorhat', callback_data='Jorhat-54'),
            InlineKeyboardButton('Kamrup Metropolitan', callback_data='Kamrup Metropolitan-49'),
        ],
        [
            InlineKeyboardButton('Kamrup Rural', callback_data='Kamrup Rural-50'),
            InlineKeyboardButton('Karbi-Anglong', callback_data='Karbi-Anglong-51'),
        ],
        [
            InlineKeyboardButton('Karimganj', callback_data='Karimganj-69'),
            InlineKeyboardButton('Kokrajhar', callback_data='Kokrajhar-61'),
        ],
        [
            InlineKeyboardButton('Lakhimpur', callback_data='Lakhimpur-63'),
            InlineKeyboardButton('Majuli', callback_data='Majuli-767'),
        ],
        [
            InlineKeyboardButton('Morigaon', callback_data='Morigaon-55'),
            InlineKeyboardButton('Nagaon', callback_data='Nagaon-56'),
        ],
        [
            InlineKeyboardButton('Nalbari', callback_data='Nalbari-52'),
            InlineKeyboardButton('Sivasagar', callback_data='Sivasagar-44'),
        ],
        [
            InlineKeyboardButton('Sonitpur', callback_data='Sonitpur-64'),
            InlineKeyboardButton('South Salmara Mankachar', callback_data='South Salmara Mankachar-768'),
        ],
        [
            InlineKeyboardButton('Tinsukia', callback_data='Tinsukia-45'),
            InlineKeyboardButton('Udalguri', callback_data='Udalguri-65'),
        ],
        [
            InlineKeyboardButton('West Karbi Anglong', callback_data='West Karbi Anglong-769'),
        ]
    ]


    return InlineKeyboardMarkup(keyboard)

def get_district_5() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Araria', callback_data='Araria-74'),
            InlineKeyboardButton('Arwal', callback_data='Arwal-78'),
        ],
        [
            InlineKeyboardButton('Aurangabad', callback_data='Aurangabad-77'),
            InlineKeyboardButton('Banka', callback_data='Banka-83'),
        ],
        [
            InlineKeyboardButton('Begusarai', callback_data='Begusarai-98'),
            InlineKeyboardButton('Bhagalpur', callback_data='Bhagalpur-82'),
        ],
        [
            InlineKeyboardButton('Bhojpur', callback_data='Bhojpur-99'),
            InlineKeyboardButton('Buxar', callback_data='Buxar-100'),
        ],
        [
            InlineKeyboardButton('Darbhanga', callback_data='Darbhanga-94'),
            InlineKeyboardButton('East Champaran', callback_data='East Champaran-105'),
        ],
        [
            InlineKeyboardButton('Gaya', callback_data='Gaya-79'),
            InlineKeyboardButton('Gopalganj', callback_data='Gopalganj-104'),
        ],
        [
            InlineKeyboardButton('Jamui', callback_data='Jamui-107'),
            InlineKeyboardButton('Jehanabad', callback_data='Jehanabad-91'),
        ],
        [
            InlineKeyboardButton('Kaimur', callback_data='Kaimur-80'),
            InlineKeyboardButton('Katihar', callback_data='Katihar-75'),
        ],
        [
            InlineKeyboardButton('Khagaria', callback_data='Khagaria-101'),
            InlineKeyboardButton('Kishanganj', callback_data='Kishanganj-76'),
        ],
        [
            InlineKeyboardButton('Lakhisarai', callback_data='Lakhisarai-84'),
            InlineKeyboardButton('Madhepura', callback_data='Madhepura-70'),
        ],
        [
            InlineKeyboardButton('Madhubani', callback_data='Madhubani-95'),
            InlineKeyboardButton('Munger', callback_data='Munger-85'),
        ],
        [
            InlineKeyboardButton('Muzaffarpur', callback_data='Muzaffarpur-86'),
            InlineKeyboardButton('Nalanda', callback_data='Nalanda-90'),
        ],
        [
            InlineKeyboardButton('Nawada', callback_data='Nawada-92'),
            InlineKeyboardButton('Patna', callback_data='Patna-97'),
        ],
        [
            InlineKeyboardButton('Purnia', callback_data='Purnia-73'),
            InlineKeyboardButton('Rohtas', callback_data='Rohtas-81'),
        ],
        [
            InlineKeyboardButton('Saharsa', callback_data='Saharsa-71'),
            InlineKeyboardButton('Samastipur', callback_data='Samastipur-96'),
        ],
        [
            InlineKeyboardButton('Saran', callback_data='Saran-102'),
            InlineKeyboardButton('Sheikhpura', callback_data='Sheikhpura-93'),
        ],
        [
            InlineKeyboardButton('Sheohar', callback_data='Sheohar-87'),
            InlineKeyboardButton('Sitamarhi', callback_data='Sitamarhi-88'),
        ],
        [
            InlineKeyboardButton('Siwan', callback_data='Siwan-103'),
            InlineKeyboardButton('Supaul', callback_data='Supaul-72'),
        ],
        [
            InlineKeyboardButton('Vaishali', callback_data='Vaishali-89'),
            InlineKeyboardButton('West Champaran', callback_data='West Champaran-106'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_6() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Chandigarh', callback_data='Chandigarh-108'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_7() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Balod', callback_data='Balod-110'),
            InlineKeyboardButton('Baloda bazar', callback_data='Baloda bazar-111'),
        ],
        [
            InlineKeyboardButton('Balrampur', callback_data='Balrampur-112'),
            InlineKeyboardButton('Bastar', callback_data='Bastar-113'),
        ],
        [
            InlineKeyboardButton('Bemetara', callback_data='Bemetara-114'),
            InlineKeyboardButton('Bijapur', callback_data='Bijapur-115'),
        ],
        [
            InlineKeyboardButton('Bilaspur', callback_data='Bilaspur-116'),
            InlineKeyboardButton('Dantewada', callback_data='Dantewada-117'),
        ],
        [
            InlineKeyboardButton('Dhamtari', callback_data='Dhamtari-118'),
            InlineKeyboardButton('Durg', callback_data='Durg-119'),
        ],
        [
            InlineKeyboardButton('Gariaband', callback_data='Gariaband-120'),
            InlineKeyboardButton('Gaurela Pendra Marwahi ', callback_data='Gaurela Pendra Marwahi -136'),
        ],
        [
            InlineKeyboardButton('Janjgir-Champa', callback_data='Janjgir-Champa-121'),
            InlineKeyboardButton('Jashpur', callback_data='Jashpur-122'),
        ],
        [
            InlineKeyboardButton('Kanker', callback_data='Kanker-123'),
            InlineKeyboardButton('Kawardha', callback_data='Kawardha-135'),
        ],
        [
            InlineKeyboardButton('Kondagaon', callback_data='Kondagaon-124'),
            InlineKeyboardButton('Korba', callback_data='Korba-125'),
        ],
        [
            InlineKeyboardButton('Koriya', callback_data='Koriya-126'),
            InlineKeyboardButton('Mahasamund', callback_data='Mahasamund-127'),
        ],
        [
            InlineKeyboardButton('Mungeli', callback_data='Mungeli-128'),
            InlineKeyboardButton('Narayanpur', callback_data='Narayanpur-129'),
        ],
        [
            InlineKeyboardButton('Raigarh', callback_data='Raigarh-130'),
            InlineKeyboardButton('Raipur', callback_data='Raipur-109'),
        ],
        [
            InlineKeyboardButton('Rajnandgaon', callback_data='Rajnandgaon-131'),
            InlineKeyboardButton('Sukma', callback_data='Sukma-132'),
        ],
        [
            InlineKeyboardButton('Surajpur', callback_data='Surajpur-133'),
            InlineKeyboardButton('Surguja', callback_data='Surguja-134'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_8() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Dadra and Nagar Haveli', callback_data='Dadra and Nagar Haveli-137'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_9() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Central Delhi', callback_data='Central Delhi-141'),
            InlineKeyboardButton('East Delhi', callback_data='East Delhi-145'),
        ],
        [
            InlineKeyboardButton('New Delhi', callback_data='New Delhi-140'),
            InlineKeyboardButton('North Delhi', callback_data='North Delhi-146'),
        ],
        [
            InlineKeyboardButton('North East Delhi', callback_data='North East Delhi-147'),
            InlineKeyboardButton('North West Delhi', callback_data='North West Delhi-143'),
        ],
        [
            InlineKeyboardButton('Shahdara', callback_data='Shahdara-148'),
            InlineKeyboardButton('South Delhi', callback_data='South Delhi-149'),
        ],
        [
            InlineKeyboardButton('South East Delhi', callback_data='South East Delhi-144'),
            InlineKeyboardButton('South West Delhi', callback_data='South West Delhi-150'),
        ],
        [
            InlineKeyboardButton('West Delhi', callback_data='West Delhi-142'),
        ]
    ]


    return InlineKeyboardMarkup(keyboard)

def get_district_10() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('North Goa', callback_data='North Goa-151'),
            InlineKeyboardButton('South Goa', callback_data='South Goa-152'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_11() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Ahmedabad', callback_data='Ahmedabad-154'),
            InlineKeyboardButton('Ahmedabad Corporation', callback_data='Ahmedabad Corporation-770'),
        ],
        [
            InlineKeyboardButton('Amreli', callback_data='Amreli-174'),
            InlineKeyboardButton('Anand', callback_data='Anand-179'),
        ],
        [
            InlineKeyboardButton('Aravalli', callback_data='Aravalli-158'),
            InlineKeyboardButton('Banaskantha', callback_data='Banaskantha-159'),
        ],
        [
            InlineKeyboardButton('Bharuch', callback_data='Bharuch-180'),
            InlineKeyboardButton('Bhavnagar', callback_data='Bhavnagar-175'),
        ],
        [
            InlineKeyboardButton('Bhavnagar Corporation', callback_data='Bhavnagar Corporation-771'),
            InlineKeyboardButton('Botad', callback_data='Botad-176'),
        ],
        [
            InlineKeyboardButton('Chhotaudepur', callback_data='Chhotaudepur-181'),
            InlineKeyboardButton('Dahod', callback_data='Dahod-182'),
        ],
        [
            InlineKeyboardButton('Dang', callback_data='Dang-163'),
            InlineKeyboardButton('Devbhumi Dwaraka', callback_data='Devbhumi Dwaraka-168'),
        ],
        [
            InlineKeyboardButton('Gandhinagar', callback_data='Gandhinagar-153'),
            InlineKeyboardButton('Gandhinagar Corporation', callback_data='Gandhinagar Corporation-772'),
        ],
        [
            InlineKeyboardButton('Gir Somnath', callback_data='Gir Somnath-177'),
            InlineKeyboardButton('Jamnagar', callback_data='Jamnagar-169'),
        ],
        [
            InlineKeyboardButton('Jamnagar Corporation', callback_data='Jamnagar Corporation-773'),
            InlineKeyboardButton('Junagadh', callback_data='Junagadh-178'),
        ],
        [
            InlineKeyboardButton('Junagadh Corporation', callback_data='Junagadh Corporation-774'),
            InlineKeyboardButton('Kheda', callback_data='Kheda-156'),
        ],
        [
            InlineKeyboardButton('Kutch', callback_data='Kutch-170'),
            InlineKeyboardButton('Mahisagar', callback_data='Mahisagar-183'),
        ],
        [
            InlineKeyboardButton('Mehsana', callback_data='Mehsana-160'),
            InlineKeyboardButton('Morbi', callback_data='Morbi-171'),
        ],
        [
            InlineKeyboardButton('Narmada', callback_data='Narmada-184'),
            InlineKeyboardButton('Navsari', callback_data='Navsari-164'),
        ],
        [
            InlineKeyboardButton('Panchmahal', callback_data='Panchmahal-185'),
            InlineKeyboardButton('Patan', callback_data='Patan-161'),
        ],
        [
            InlineKeyboardButton('Porbandar', callback_data='Porbandar-172'),
            InlineKeyboardButton('Rajkot', callback_data='Rajkot-173'),
        ],
        [
            InlineKeyboardButton('Rajkot Corporation', callback_data='Rajkot Corporation-775'),
            InlineKeyboardButton('Sabarkantha', callback_data='Sabarkantha-162'),
        ],
        [
            InlineKeyboardButton('Surat', callback_data='Surat-165'),
            InlineKeyboardButton('Surat Corporation', callback_data='Surat Corporation-776'),
        ],
        [
            InlineKeyboardButton('Surendranagar', callback_data='Surendranagar-157'),
            InlineKeyboardButton('Tapi', callback_data='Tapi-166'),
        ],
        [
            InlineKeyboardButton('Vadodara', callback_data='Vadodara-155'),
            InlineKeyboardButton('Vadodara Corporation', callback_data='Vadodara Corporation-777'),
        ],
        [
            InlineKeyboardButton('Valsad', callback_data='Valsad-167'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_12() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Ambala', callback_data='Ambala-193'),
            InlineKeyboardButton('Bhiwani', callback_data='Bhiwani-200'),
        ],
        [
            InlineKeyboardButton('Charkhi Dadri', callback_data='Charkhi Dadri-201'),
            InlineKeyboardButton('Faridabad', callback_data='Faridabad-199'),
        ],
        [
            InlineKeyboardButton('Fatehabad', callback_data='Fatehabad-196'),
            InlineKeyboardButton('Gurgaon', callback_data='Gurgaon-188'),
        ],
        [
            InlineKeyboardButton('Hisar', callback_data='Hisar-191'),
            InlineKeyboardButton('Jhajjar', callback_data='Jhajjar-189'),
        ],
        [
            InlineKeyboardButton('Jind', callback_data='Jind-204'),
            InlineKeyboardButton('Kaithal', callback_data='Kaithal-190'),
        ],
        [
            InlineKeyboardButton('Karnal', callback_data='Karnal-203'),
            InlineKeyboardButton('Kurukshetra', callback_data='Kurukshetra-186'),
        ],
        [
            InlineKeyboardButton('Mahendragarh', callback_data='Mahendragarh-206'),
            InlineKeyboardButton('Nuh', callback_data='Nuh-205'),
        ],
        [
            InlineKeyboardButton('Palwal', callback_data='Palwal-207'),
            InlineKeyboardButton('Panchkula', callback_data='Panchkula-187'),
        ],
        [
            InlineKeyboardButton('Panipat', callback_data='Panipat-195'),
            InlineKeyboardButton('Rewari', callback_data='Rewari-202'),
        ],
        [
            InlineKeyboardButton('Rohtak', callback_data='Rohtak-192'),
            InlineKeyboardButton('Sirsa', callback_data='Sirsa-194'),
        ],
        [
            InlineKeyboardButton('Sonipat', callback_data='Sonipat-198'),
            InlineKeyboardButton('Yamunanagar', callback_data='Yamunanagar-197'),
        ]

    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_13() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Bilaspur', callback_data='Bilaspur-219'),
            InlineKeyboardButton('Chamba', callback_data='Chamba-214'),
        ],
        [
            InlineKeyboardButton('Hamirpur', callback_data='Hamirpur-217'),
            InlineKeyboardButton('Kangra', callback_data='Kangra-213'),
        ],
        [
            InlineKeyboardButton('Kinnaur', callback_data='Kinnaur-216'),
            InlineKeyboardButton('Kullu', callback_data='Kullu-211'),
        ],
        [
            InlineKeyboardButton('Lahaul Spiti', callback_data='Lahaul Spiti-210'),
            InlineKeyboardButton('Mandi', callback_data='Mandi-215'),
        ],
        [
            InlineKeyboardButton('Shimla', callback_data='Shimla-208'),
            InlineKeyboardButton('Sirmaur', callback_data='Sirmaur-212'),
        ],
        [
            InlineKeyboardButton('Solan', callback_data='Solan-209'),
            InlineKeyboardButton('Una', callback_data='Una-218'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_14() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Anantnag', callback_data='Anantnag-224'),
            InlineKeyboardButton('Bandipore', callback_data='Bandipore-223'),
        ],
        [
            InlineKeyboardButton('Baramulla', callback_data='Baramulla-225'),
            InlineKeyboardButton('Budgam', callback_data='Budgam-229'),
        ],
        [
            InlineKeyboardButton('Doda', callback_data='Doda-232'),
            InlineKeyboardButton('Ganderbal', callback_data='Ganderbal-228'),
        ],
        [
            InlineKeyboardButton('Jammu', callback_data='Jammu-230'),
            InlineKeyboardButton('Kathua', callback_data='Kathua-234'),
        ],
        [
            InlineKeyboardButton('Kishtwar', callback_data='Kishtwar-231'),
            InlineKeyboardButton('Kulgam', callback_data='Kulgam-221'),
        ],
        [
            InlineKeyboardButton('Kupwara', callback_data='Kupwara-226'),
            InlineKeyboardButton('Poonch', callback_data='Poonch-238'),
        ],
        [
            InlineKeyboardButton('Pulwama', callback_data='Pulwama-227'),
            InlineKeyboardButton('Rajouri', callback_data='Rajouri-237'),
        ],
        [
            InlineKeyboardButton('Ramban', callback_data='Ramban-235'),
            InlineKeyboardButton('Reasi', callback_data='Reasi-239'),
        ],
        [
            InlineKeyboardButton('Samba', callback_data='Samba-236'),
            InlineKeyboardButton('Shopian', callback_data='Shopian-222'),
        ],
        [
            InlineKeyboardButton('Srinagar', callback_data='Srinagar-220'),
            InlineKeyboardButton('Udhampur', callback_data='Udhampur-233'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_15() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Bokaro', callback_data='Bokaro-242'),
            InlineKeyboardButton('Chatra', callback_data='Chatra-245'),
        ],
        [
            InlineKeyboardButton('Deoghar', callback_data='Deoghar-253'),
            InlineKeyboardButton('Dhanbad', callback_data='Dhanbad-257'),
        ],
        [
            InlineKeyboardButton('Dumka', callback_data='Dumka-258'),
            InlineKeyboardButton('East Singhbhum', callback_data='East Singhbhum-247'),
        ],
        [
            InlineKeyboardButton('Garhwa', callback_data='Garhwa-243'),
            InlineKeyboardButton('Giridih', callback_data='Giridih-256'),
        ],
        [
            InlineKeyboardButton('Godda', callback_data='Godda-262'),
            InlineKeyboardButton('Gumla', callback_data='Gumla-251'),
        ],
        [
            InlineKeyboardButton('Hazaribagh', callback_data='Hazaribagh-255'),
            InlineKeyboardButton('Jamtara', callback_data='Jamtara-259'),
        ],
        [
            InlineKeyboardButton('Khunti', callback_data='Khunti-252'),
            InlineKeyboardButton('Koderma', callback_data='Koderma-241'),
        ],
        [
            InlineKeyboardButton('Latehar', callback_data='Latehar-244'),
            InlineKeyboardButton('Lohardaga', callback_data='Lohardaga-250'),
        ],
        [
            InlineKeyboardButton('Pakur', callback_data='Pakur-261'),
            InlineKeyboardButton('Palamu', callback_data='Palamu-246'),
        ],
        [
            InlineKeyboardButton('Ramgarh', callback_data='Ramgarh-254'),
            InlineKeyboardButton('Ranchi', callback_data='Ranchi-240'),
        ],
        [
            InlineKeyboardButton('Sahebganj', callback_data='Sahebganj-260'),
            InlineKeyboardButton('Seraikela Kharsawan', callback_data='Seraikela Kharsawan-248'),
        ],
        [
            InlineKeyboardButton('Simdega', callback_data='Simdega-249'),
            InlineKeyboardButton('West Singhbhum', callback_data='West Singhbhum-263'),
        ]

    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_16() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Bagalkot', callback_data='Bagalkot-270'),
            InlineKeyboardButton('Bangalore Rural', callback_data='Bangalore Rural-276'),
        ],
        [
            InlineKeyboardButton('Bangalore Urban', callback_data='Bangalore Urban-265'),
            InlineKeyboardButton('BBMP', callback_data='BBMP-294'),
        ],
        [
            InlineKeyboardButton('Belgaum', callback_data='Belgaum-264'),
            InlineKeyboardButton('Bellary', callback_data='Bellary-274'),
        ],
        [
            InlineKeyboardButton('Bidar', callback_data='Bidar-272'),
            InlineKeyboardButton('Chamarajanagar', callback_data='Chamarajanagar-271'),
        ],
        [
            InlineKeyboardButton('Chikamagalur', callback_data='Chikamagalur-273'),
            InlineKeyboardButton('Chikkaballapur', callback_data='Chikkaballapur-291'),
        ],
        [
            InlineKeyboardButton('Chitradurga', callback_data='Chitradurga-268'),
            InlineKeyboardButton('Dakshina Kannada', callback_data='Dakshina Kannada-269'),
        ],
        [
            InlineKeyboardButton('Davanagere', callback_data='Davanagere-275'),
            InlineKeyboardButton('Dharwad', callback_data='Dharwad-278'),
        ],
        [
            InlineKeyboardButton('Gadag', callback_data='Gadag-280'),
            InlineKeyboardButton('Gulbarga', callback_data='Gulbarga-267'),
        ],
        [
            InlineKeyboardButton('Hassan', callback_data='Hassan-289'),
            InlineKeyboardButton('Haveri', callback_data='Haveri-279'),
        ],
        [
            InlineKeyboardButton('Kodagu', callback_data='Kodagu-283'),
            InlineKeyboardButton('Kolar', callback_data='Kolar-277'),
        ],
        [
            InlineKeyboardButton('Koppal', callback_data='Koppal-282'),
            InlineKeyboardButton('Mandya', callback_data='Mandya-290'),
        ],
        [
            InlineKeyboardButton('Mysore', callback_data='Mysore-266'),
            InlineKeyboardButton('Raichur', callback_data='Raichur-284'),
        ],
        [
            InlineKeyboardButton('Ramanagara', callback_data='Ramanagara-292'),
            InlineKeyboardButton('Shimoga', callback_data='Shimoga-287'),
        ],
        [
            InlineKeyboardButton('Tumkur', callback_data='Tumkur-288'),
            InlineKeyboardButton('Udupi', callback_data='Udupi-286'),
        ],
        [
            InlineKeyboardButton('Uttar Kannada', callback_data='Uttar Kannada-281'),
            InlineKeyboardButton('Vijayapura', callback_data='Vijayapura-293'),
        ],
        [
            InlineKeyboardButton('Yadgir', callback_data='Yadgir-285'),
        ]
    ]


    return InlineKeyboardMarkup(keyboard)

def get_district_17() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Alappuzha', callback_data='Alappuzha-301'),
            InlineKeyboardButton('Ernakulam', callback_data='Ernakulam-307'),
        ],
        [
            InlineKeyboardButton('Idukki', callback_data='Idukki-306'),
            InlineKeyboardButton('Kannur', callback_data='Kannur-297'),
        ],
        [
            InlineKeyboardButton('Kasaragod', callback_data='Kasaragod-295'),
            InlineKeyboardButton('Kollam', callback_data='Kollam-298'),
        ],
        [
            InlineKeyboardButton('Kottayam', callback_data='Kottayam-304'),
            InlineKeyboardButton('Kozhikode', callback_data='Kozhikode-305'),
        ],
        [
            InlineKeyboardButton('Malappuram', callback_data='Malappuram-302'),
            InlineKeyboardButton('Palakkad', callback_data='Palakkad-308'),
        ],
        [
            InlineKeyboardButton('Pathanamthitta', callback_data='Pathanamthitta-300'),
            InlineKeyboardButton('Thiruvananthapuram', callback_data='Thiruvananthapuram-296'),
        ],
        [
            InlineKeyboardButton('Thrissur', callback_data='Thrissur-303'),
            InlineKeyboardButton('Wayanad', callback_data='Wayanad-299'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_18() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Kargil', callback_data='Kargil-309'),
            InlineKeyboardButton('Leh', callback_data='Leh-310'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_19() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Agatti Island', callback_data='Agatti Island-796'),
            InlineKeyboardButton('Lakshadweep', callback_data='Lakshadweep-311'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_20() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Agar', callback_data='Agar-320'),
            InlineKeyboardButton('Alirajpur', callback_data='Alirajpur-357'),
        ],
        [
            InlineKeyboardButton('Anuppur', callback_data='Anuppur-334'),
            InlineKeyboardButton('Ashoknagar', callback_data='Ashoknagar-354'),
        ],
        [
            InlineKeyboardButton('Balaghat', callback_data='Balaghat-338'),
            InlineKeyboardButton('Barwani', callback_data='Barwani-343'),
        ],
        [
            InlineKeyboardButton('Betul', callback_data='Betul-362'),
            InlineKeyboardButton('Bhind', callback_data='Bhind-351'),
        ],
        [
            InlineKeyboardButton('Bhopal', callback_data='Bhopal-312'),
            InlineKeyboardButton('Burhanpur', callback_data='Burhanpur-342'),
        ],
        [
            InlineKeyboardButton('Chhatarpur', callback_data='Chhatarpur-328'),
            InlineKeyboardButton('Chhindwara', callback_data='Chhindwara-337'),
        ],
        [
            InlineKeyboardButton('Damoh', callback_data='Damoh-327'),
            InlineKeyboardButton('Datia', callback_data='Datia-350'),
        ],
        [
            InlineKeyboardButton('Dewas', callback_data='Dewas-324'),
            InlineKeyboardButton('Dhar', callback_data='Dhar-341'),
        ],
        [
            InlineKeyboardButton('Dindori', callback_data='Dindori-336'),
            InlineKeyboardButton('Guna', callback_data='Guna-348'),
        ],
        [
            InlineKeyboardButton('Gwalior', callback_data='Gwalior-313'),
            InlineKeyboardButton('Harda', callback_data='Harda-361'),
        ],
        [
            InlineKeyboardButton('Hoshangabad', callback_data='Hoshangabad-360'),
            InlineKeyboardButton('Indore', callback_data='Indore-314'),
        ],
        [
            InlineKeyboardButton('Jabalpur', callback_data='Jabalpur-315'),
            InlineKeyboardButton('Jhabua', callback_data='Jhabua-340'),
        ],
        [
            InlineKeyboardButton('Katni', callback_data='Katni-353'),
            InlineKeyboardButton('Khandwa', callback_data='Khandwa-339'),
        ],
        [
            InlineKeyboardButton('Khargone', callback_data='Khargone-344'),
            InlineKeyboardButton('Mandla', callback_data='Mandla-335'),
        ],
        [
            InlineKeyboardButton('Mandsaur', callback_data='Mandsaur-319'),
            InlineKeyboardButton('Morena', callback_data='Morena-347'),
        ],
        [
            InlineKeyboardButton('Narsinghpur', callback_data='Narsinghpur-352'),
            InlineKeyboardButton('Neemuch', callback_data='Neemuch-323'),
        ],
        [
            InlineKeyboardButton('Panna', callback_data='Panna-326'),
            InlineKeyboardButton('Raisen', callback_data='Raisen-359'),
        ],
        [
            InlineKeyboardButton('Rajgarh', callback_data='Rajgarh-358'),
            InlineKeyboardButton('Ratlam', callback_data='Ratlam-322'),
        ],
        [
            InlineKeyboardButton('Rewa', callback_data='Rewa-316'),
            InlineKeyboardButton('Sagar', callback_data='Sagar-317'),
        ],
        [
            InlineKeyboardButton('Satna', callback_data='Satna-333'),
            InlineKeyboardButton('Sehore', callback_data='Sehore-356'),
        ],
        [
            InlineKeyboardButton('Seoni', callback_data='Seoni-349'),
            InlineKeyboardButton('Shahdol', callback_data='Shahdol-332'),
        ],
        [
            InlineKeyboardButton('Shajapur', callback_data='Shajapur-321'),
            InlineKeyboardButton('Sheopur', callback_data='Sheopur-346'),
        ],
        [
            InlineKeyboardButton('Shivpuri', callback_data='Shivpuri-345'),
            InlineKeyboardButton('Sidhi', callback_data='Sidhi-331'),
        ],
        [
            InlineKeyboardButton('Singrauli', callback_data='Singrauli-330'),
            InlineKeyboardButton('Tikamgarh', callback_data='Tikamgarh-325'),
        ],
        [
            InlineKeyboardButton('Ujjain', callback_data='Ujjain-318'),
            InlineKeyboardButton('Umaria', callback_data='Umaria-329'),
        ],
        [
            InlineKeyboardButton('Vidisha', callback_data='Vidisha-355'),
        ]
    ]


    return InlineKeyboardMarkup(keyboard)

def get_district_21() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Ahmednagar', callback_data='Ahmednagar-391'),
            InlineKeyboardButton('Akola', callback_data='Akola-364'),
        ],
        [
            InlineKeyboardButton('Amravati', callback_data='Amravati-366'),
            InlineKeyboardButton('Aurangabad ', callback_data='Aurangabad -397'),
        ],
        [
            InlineKeyboardButton('Beed', callback_data='Beed-384'),
            InlineKeyboardButton('Bhandara', callback_data='Bhandara-370'),
        ],
        [
            InlineKeyboardButton('Buldhana', callback_data='Buldhana-367'),
            InlineKeyboardButton('Chandrapur', callback_data='Chandrapur-380'),
        ],
        [
            InlineKeyboardButton('Dhule', callback_data='Dhule-388'),
            InlineKeyboardButton('Gadchiroli', callback_data='Gadchiroli-379'),
        ],
        [
            InlineKeyboardButton('Gondia', callback_data='Gondia-378'),
            InlineKeyboardButton('Hingoli', callback_data='Hingoli-386'),
        ],
        [
            InlineKeyboardButton('Jalgaon', callback_data='Jalgaon-390'),
            InlineKeyboardButton('Jalna', callback_data='Jalna-396'),
        ],
        [
            InlineKeyboardButton('Kolhapur', callback_data='Kolhapur-371'),
            InlineKeyboardButton('Latur', callback_data='Latur-383'),
        ],
        [
            InlineKeyboardButton('Mumbai', callback_data='Mumbai-395'),
            InlineKeyboardButton('Nagpur', callback_data='Nagpur-365'),
        ],
        [
            InlineKeyboardButton('Nanded', callback_data='Nanded-382'),
            InlineKeyboardButton('Nandurbar', callback_data='Nandurbar-387'),
        ],
        [
            InlineKeyboardButton('Nashik', callback_data='Nashik-389'),
            InlineKeyboardButton('Osmanabad', callback_data='Osmanabad-381'),
        ],
        [
            InlineKeyboardButton('Palghar', callback_data='Palghar-394'),
            InlineKeyboardButton('Parbhani', callback_data='Parbhani-385'),
        ],
        [
            InlineKeyboardButton('Pune', callback_data='Pune-363'),
            InlineKeyboardButton('Raigad', callback_data='Raigad-393'),
        ],
        [
            InlineKeyboardButton('Ratnagiri', callback_data='Ratnagiri-372'),
            InlineKeyboardButton('Sangli', callback_data='Sangli-373'),
        ],
        [
            InlineKeyboardButton('Satara', callback_data='Satara-376'),
            InlineKeyboardButton('Sindhudurg', callback_data='Sindhudurg-374'),
        ],
        [
            InlineKeyboardButton('Solapur', callback_data='Solapur-375'),
            InlineKeyboardButton('Thane', callback_data='Thane-392'),
        ],
        [
            InlineKeyboardButton('Wardha', callback_data='Wardha-377'),
            InlineKeyboardButton('Washim', callback_data='Washim-369'),
        ],
        [
            InlineKeyboardButton('Yavatmal', callback_data='Yavatmal-368'),
        ]
    ]


    return InlineKeyboardMarkup(keyboard)

def get_district_22() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Bishnupur', callback_data='Bishnupur-398'),
            InlineKeyboardButton('Chandel', callback_data='Chandel-399'),
        ],
        [
            InlineKeyboardButton('Churachandpur', callback_data='Churachandpur-400'),
            InlineKeyboardButton('Imphal East', callback_data='Imphal East-401'),
        ],
        [
            InlineKeyboardButton('Imphal West', callback_data='Imphal West-402'),
            InlineKeyboardButton('Jiribam', callback_data='Jiribam-410'),
        ],
        [
            InlineKeyboardButton('Kakching', callback_data='Kakching-413'),
            InlineKeyboardButton('Kamjong', callback_data='Kamjong-409'),
        ],
        [
            InlineKeyboardButton('Kangpokpi', callback_data='Kangpokpi-408'),
            InlineKeyboardButton('Noney', callback_data='Noney-412'),
        ],
        [
            InlineKeyboardButton('Pherzawl', callback_data='Pherzawl-411'),
            InlineKeyboardButton('Senapati', callback_data='Senapati-403'),
        ],
        [
            InlineKeyboardButton('Tamenglong', callback_data='Tamenglong-404'),
            InlineKeyboardButton('Tengnoupal', callback_data='Tengnoupal-407'),
        ],
        [
            InlineKeyboardButton('Thoubal', callback_data='Thoubal-405'),
            InlineKeyboardButton('Ukhrul', callback_data='Ukhrul-406'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_23() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('East Garo Hills', callback_data='East Garo Hills-424'),
            InlineKeyboardButton('East Jaintia Hills', callback_data='East Jaintia Hills-418'),
        ],
        [
            InlineKeyboardButton('East Khasi Hills', callback_data='East Khasi Hills-414'),
            InlineKeyboardButton('North Garo Hills', callback_data='North Garo Hills-423'),
        ],
        [
            InlineKeyboardButton('Ri-Bhoi', callback_data='Ri-Bhoi-417'),
            InlineKeyboardButton('South Garo Hills', callback_data='South Garo Hills-421'),
        ],
        [
            InlineKeyboardButton('South West Garo Hills', callback_data='South West Garo Hills-422'),
            InlineKeyboardButton('South West Khasi Hills', callback_data='South West Khasi Hills-415'),
        ],
        [
            InlineKeyboardButton('West Garo Hills', callback_data='West Garo Hills-420'),
            InlineKeyboardButton('West Jaintia Hills', callback_data='West Jaintia Hills-416'),
        ],
        [
            InlineKeyboardButton('West Khasi Hills', callback_data='West Khasi Hills-419'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_24() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Aizawl East', callback_data='Aizawl East-425'),
            InlineKeyboardButton('Aizawl West', callback_data='Aizawl West-426'),
        ],
        [
            InlineKeyboardButton('Champhai', callback_data='Champhai-429'),
            InlineKeyboardButton('Kolasib', callback_data='Kolasib-428'),
        ],
        [
            InlineKeyboardButton('Lawngtlai', callback_data='Lawngtlai-432'),
            InlineKeyboardButton('Lunglei', callback_data='Lunglei-431'),
        ],
        [
            InlineKeyboardButton('Mamit', callback_data='Mamit-427'),
            InlineKeyboardButton('Serchhip', callback_data='Serchhip-430'),
        ],
        [
            InlineKeyboardButton('Siaha', callback_data='Siaha-433'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_25() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Dimapur', callback_data='Dimapur-434'),
            InlineKeyboardButton('Kiphire', callback_data='Kiphire-444'),
        ],
        [
            InlineKeyboardButton('Kohima', callback_data='Kohima-441'),
            InlineKeyboardButton('Longleng', callback_data='Longleng-438'),
        ],
        [
            InlineKeyboardButton('Mokokchung', callback_data='Mokokchung-437'),
            InlineKeyboardButton('Mon', callback_data='Mon-439'),
        ],
        [
            InlineKeyboardButton('Peren', callback_data='Peren-435'),
            InlineKeyboardButton('Phek', callback_data='Phek-443'),
        ],
        [
            InlineKeyboardButton('Tuensang', callback_data='Tuensang-440'),
            InlineKeyboardButton('Wokha', callback_data='Wokha-436'),
        ],
        [
            InlineKeyboardButton('Zunheboto', callback_data='Zunheboto-442'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_26() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Angul', callback_data='Angul-445'),
            InlineKeyboardButton('Balangir', callback_data='Balangir-448'),
        ],
        [
            InlineKeyboardButton('Balasore', callback_data='Balasore-447'),
            InlineKeyboardButton('Bargarh', callback_data='Bargarh-472'),
        ],
        [
            InlineKeyboardButton('Bhadrak', callback_data='Bhadrak-454'),
            InlineKeyboardButton('Boudh', callback_data='Boudh-468'),
        ],
        [
            InlineKeyboardButton('Cuttack', callback_data='Cuttack-457'),
            InlineKeyboardButton('Deogarh', callback_data='Deogarh-473'),
        ],
        [
            InlineKeyboardButton('Dhenkanal', callback_data='Dhenkanal-458'),
            InlineKeyboardButton('Gajapati', callback_data='Gajapati-467'),
        ],
        [
            InlineKeyboardButton('Ganjam', callback_data='Ganjam-449'),
            InlineKeyboardButton('Jagatsinghpur', callback_data='Jagatsinghpur-459'),
        ],
        [
            InlineKeyboardButton('Jajpur', callback_data='Jajpur-460'),
            InlineKeyboardButton('Jharsuguda', callback_data='Jharsuguda-474'),
        ],
        [
            InlineKeyboardButton('Kalahandi', callback_data='Kalahandi-464'),
            InlineKeyboardButton('Kandhamal', callback_data='Kandhamal-450'),
        ],
        [
            InlineKeyboardButton('Kendrapara', callback_data='Kendrapara-461'),
            InlineKeyboardButton('Kendujhar', callback_data='Kendujhar-455'),
        ],
        [
            InlineKeyboardButton('Khurda', callback_data='Khurda-446'),
            InlineKeyboardButton('Koraput', callback_data='Koraput-451'),
        ],
        [
            InlineKeyboardButton('Malkangiri', callback_data='Malkangiri-469'),
            InlineKeyboardButton('Mayurbhanj', callback_data='Mayurbhanj-456'),
        ],
        [
            InlineKeyboardButton('Nabarangpur', callback_data='Nabarangpur-470'),
            InlineKeyboardButton('Nayagarh', callback_data='Nayagarh-462'),
        ],
        [
            InlineKeyboardButton('Nuapada', callback_data='Nuapada-465'),
            InlineKeyboardButton('Puri', callback_data='Puri-463'),
        ],
        [
            InlineKeyboardButton('Rayagada', callback_data='Rayagada-471'),
            InlineKeyboardButton('Sambalpur', callback_data='Sambalpur-452'),
        ],
        [
            InlineKeyboardButton('Subarnapur', callback_data='Subarnapur-466'),
            InlineKeyboardButton('Sundargarh', callback_data='Sundargarh-453'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_27() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Karaikal', callback_data='Karaikal-476'),
            InlineKeyboardButton('Mahe', callback_data='Mahe-477'),
        ],
        [
            InlineKeyboardButton('Puducherry', callback_data='Puducherry-475'),
            InlineKeyboardButton('Yanam', callback_data='Yanam-478'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_28() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Amritsar', callback_data='Amritsar-485'),
            InlineKeyboardButton('Barnala', callback_data='Barnala-483'),
        ],
        [
            InlineKeyboardButton('Bathinda', callback_data='Bathinda-493'),
            InlineKeyboardButton('Faridkot', callback_data='Faridkot-499'),
        ],
        [
            InlineKeyboardButton('Fatehgarh Sahib', callback_data='Fatehgarh Sahib-484'),
            InlineKeyboardButton('Fazilka', callback_data='Fazilka-487'),
        ],
        [
            InlineKeyboardButton('Ferozpur', callback_data='Ferozpur-480'),
            InlineKeyboardButton('Gurdaspur', callback_data='Gurdaspur-489'),
        ],
        [
            InlineKeyboardButton('Hoshiarpur', callback_data='Hoshiarpur-481'),
            InlineKeyboardButton('Jalandhar', callback_data='Jalandhar-492'),
        ],
        [
            InlineKeyboardButton('Kapurthala', callback_data='Kapurthala-479'),
            InlineKeyboardButton('Ludhiana', callback_data='Ludhiana-488'),
        ],
        [
            InlineKeyboardButton('Mansa', callback_data='Mansa-482'),
            InlineKeyboardButton('Moga', callback_data='Moga-491'),
        ],
        [
            InlineKeyboardButton('Pathankot', callback_data='Pathankot-486'),
            InlineKeyboardButton('Patiala', callback_data='Patiala-494'),
        ],
        [
            InlineKeyboardButton('Rup Nagar', callback_data='Rup Nagar-497'),
            InlineKeyboardButton('Sangrur', callback_data='Sangrur-498'),
        ],
        [
            InlineKeyboardButton('SAS Nagar', callback_data='SAS Nagar-496'),
            InlineKeyboardButton('SBS Nagar', callback_data='SBS Nagar-500'),
        ],
        [
            InlineKeyboardButton('Sri Muktsar Sahib', callback_data='Sri Muktsar Sahib-490'),
            InlineKeyboardButton('Tarn Taran', callback_data='Tarn Taran-495'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_29() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Ajmer', callback_data='Ajmer-507'),
            InlineKeyboardButton('Alwar', callback_data='Alwar-512'),
        ],
        [
            InlineKeyboardButton('Banswara', callback_data='Banswara-519'),
            InlineKeyboardButton('Baran', callback_data='Baran-516'),
        ],
        [
            InlineKeyboardButton('Barmer', callback_data='Barmer-528'),
            InlineKeyboardButton('Bharatpur', callback_data='Bharatpur-508'),
        ],
        [
            InlineKeyboardButton('Bhilwara', callback_data='Bhilwara-523'),
            InlineKeyboardButton('Bikaner', callback_data='Bikaner-501'),
        ],
        [
            InlineKeyboardButton('Bundi', callback_data='Bundi-514'),
            InlineKeyboardButton('Chittorgarh', callback_data='Chittorgarh-521'),
        ],
        [
            InlineKeyboardButton('Churu', callback_data='Churu-530'),
            InlineKeyboardButton('Dausa', callback_data='Dausa-511'),
        ],
        [
            InlineKeyboardButton('Dholpur', callback_data='Dholpur-524'),
            InlineKeyboardButton('Dungarpur', callback_data='Dungarpur-520'),
        ],
        [
            InlineKeyboardButton('Hanumangarh', callback_data='Hanumangarh-517'),
            InlineKeyboardButton('Jaipur I', callback_data='Jaipur I-505'),
        ],
        [
            InlineKeyboardButton('Jaipur II', callback_data='Jaipur II-506'),
            InlineKeyboardButton('Jaisalmer', callback_data='Jaisalmer-527'),
        ],
        [
            InlineKeyboardButton('Jalore', callback_data='Jalore-533'),
            InlineKeyboardButton('Jhalawar', callback_data='Jhalawar-515'),
        ],
        [
            InlineKeyboardButton('Jhunjhunu', callback_data='Jhunjhunu-510'),
            InlineKeyboardButton('Jodhpur', callback_data='Jodhpur-502'),
        ],
        [
            InlineKeyboardButton('Karauli', callback_data='Karauli-525'),
            InlineKeyboardButton('Kota', callback_data='Kota-503'),
        ],
        [
            InlineKeyboardButton('Nagaur', callback_data='Nagaur-532'),
            InlineKeyboardButton('Pali', callback_data='Pali-529'),
        ],
        [
            InlineKeyboardButton('Pratapgarh', callback_data='Pratapgarh-522'),
            InlineKeyboardButton('Rajsamand', callback_data='Rajsamand-518'),
        ],
        [
            InlineKeyboardButton('Sawai Madhopur', callback_data='Sawai Madhopur-534'),
            InlineKeyboardButton('Sikar', callback_data='Sikar-513'),
        ],
        [
            InlineKeyboardButton('Sirohi', callback_data='Sirohi-531'),
            InlineKeyboardButton('Sri Ganganagar', callback_data='Sri Ganganagar-509'),
        ],
        [
            InlineKeyboardButton('Tonk', callback_data='Tonk-526'),
            InlineKeyboardButton('Udaipur', callback_data='Udaipur-504'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_30() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('East Sikkim', callback_data='East Sikkim-535'),
            InlineKeyboardButton('North Sikkim', callback_data='North Sikkim-537'),
        ],
        [
            InlineKeyboardButton('South Sikkim', callback_data='South Sikkim-538'),
            InlineKeyboardButton('West Sikkim', callback_data='West Sikkim-536'),
        ]

    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_31() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Aranthangi', callback_data='Aranthangi-779'),
            InlineKeyboardButton('Ariyalur', callback_data='Ariyalur-555'),
        ],
        [
            InlineKeyboardButton('Attur', callback_data='Attur-578'),
            InlineKeyboardButton('Chengalpet', callback_data='Chengalpet-565'),
        ],
        [
            InlineKeyboardButton('Chennai', callback_data='Chennai-571'),
            InlineKeyboardButton('Cheyyar', callback_data='Cheyyar-778'),
        ],
        [
            InlineKeyboardButton('Coimbatore', callback_data='Coimbatore-539'),
            InlineKeyboardButton('Cuddalore', callback_data='Cuddalore-547'),
        ],
        [
            InlineKeyboardButton('Dharmapuri', callback_data='Dharmapuri-566'),
            InlineKeyboardButton('Dindigul', callback_data='Dindigul-556'),
        ],
        [
            InlineKeyboardButton('Erode', callback_data='Erode-563'),
            InlineKeyboardButton('Kallakurichi', callback_data='Kallakurichi-552'),
        ],
        [
            InlineKeyboardButton('Kanchipuram', callback_data='Kanchipuram-557'),
            InlineKeyboardButton('Kanyakumari', callback_data='Kanyakumari-544'),
        ],
        [
            InlineKeyboardButton('Karur', callback_data='Karur-559'),
            InlineKeyboardButton('Kovilpatti', callback_data='Kovilpatti-780'),
        ],
        [
            InlineKeyboardButton('Krishnagiri', callback_data='Krishnagiri-562'),
            InlineKeyboardButton('Madurai', callback_data='Madurai-540'),
        ],
        [
            InlineKeyboardButton('Nagapattinam', callback_data='Nagapattinam-576'),
            InlineKeyboardButton('Namakkal', callback_data='Namakkal-558'),
        ],
        [
            InlineKeyboardButton('Nilgiris', callback_data='Nilgiris-577'),
            InlineKeyboardButton('Palani', callback_data='Palani-564'),
        ],
        [
            InlineKeyboardButton('Paramakudi', callback_data='Paramakudi-573'),
            InlineKeyboardButton('Perambalur', callback_data='Perambalur-570'),
        ],
        [
            InlineKeyboardButton('Poonamallee', callback_data='Poonamallee-575'),
            InlineKeyboardButton('Pudukkottai', callback_data='Pudukkottai-546'),
        ],
        [
            InlineKeyboardButton('Ramanathapuram', callback_data='Ramanathapuram-567'),
            InlineKeyboardButton('Ranipet', callback_data='Ranipet-781'),
        ],
        [
            InlineKeyboardButton('Salem', callback_data='Salem-545'),
            InlineKeyboardButton('Sivaganga', callback_data='Sivaganga-561'),
        ],
        [
            InlineKeyboardButton('Sivakasi', callback_data='Sivakasi-580'),
            InlineKeyboardButton('Tenkasi', callback_data='Tenkasi-551'),
        ],
        [
            InlineKeyboardButton('Thanjavur', callback_data='Thanjavur-541'),
            InlineKeyboardButton('Theni', callback_data='Theni-569'),
        ],
        [
            InlineKeyboardButton('Thoothukudi (Tuticorin)', callback_data='Thoothukudi (Tuticorin)-554'),
            InlineKeyboardButton('Tiruchirappalli', callback_data='Tiruchirappalli-560'),
        ],
        [
            InlineKeyboardButton('Tirunelveli', callback_data='Tirunelveli-548'),
            InlineKeyboardButton('Tirupattur', callback_data='Tirupattur-550'),
        ],
        [
            InlineKeyboardButton('Tiruppur', callback_data='Tiruppur-568'),
            InlineKeyboardButton('Tiruvallur', callback_data='Tiruvallur-572'),
        ],
        [
            InlineKeyboardButton('Tiruvannamalai', callback_data='Tiruvannamalai-553'),
            InlineKeyboardButton('Tiruvarur', callback_data='Tiruvarur-574'),
        ],
        [
            InlineKeyboardButton('Vellore', callback_data='Vellore-543'),
            InlineKeyboardButton('Viluppuram', callback_data='Viluppuram-542'),
        ],
        [
            InlineKeyboardButton('Virudhunagar', callback_data='Virudhunagar-549'),
        ]
    ]


    return InlineKeyboardMarkup(keyboard)

def get_district_32() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Adilabad', callback_data='Adilabad-582'),
            InlineKeyboardButton('Bhadradri Kothagudem', callback_data='Bhadradri Kothagudem-583'),
        ],
        [
            InlineKeyboardButton('Hyderabad', callback_data='Hyderabad-581'),
            InlineKeyboardButton('Jagtial', callback_data='Jagtial-584'),
        ],
        [
            InlineKeyboardButton('Jangaon', callback_data='Jangaon-585'),
            InlineKeyboardButton('Jayashankar Bhupalpally', callback_data='Jayashankar Bhupalpally-586'),
        ],
        [
            InlineKeyboardButton('Jogulamba Gadwal', callback_data='Jogulamba Gadwal-587'),
            InlineKeyboardButton('Kamareddy', callback_data='Kamareddy-588'),
        ],
        [
            InlineKeyboardButton('Karimnagar', callback_data='Karimnagar-589'),
            InlineKeyboardButton('Khammam', callback_data='Khammam-590'),
        ],
        [
            InlineKeyboardButton('Kumuram Bheem', callback_data='Kumuram Bheem-591'),
            InlineKeyboardButton('Mahabubabad', callback_data='Mahabubabad-592'),
        ],
        [
            InlineKeyboardButton('Mahabubnagar', callback_data='Mahabubnagar-593'),
            InlineKeyboardButton('Mancherial', callback_data='Mancherial-594'),
        ],
        [
            InlineKeyboardButton('Medak', callback_data='Medak-595'),
            InlineKeyboardButton('Medchal', callback_data='Medchal-596'),
        ],
        [
            InlineKeyboardButton('Mulugu', callback_data='Mulugu-612'),
            InlineKeyboardButton('Nagarkurnool', callback_data='Nagarkurnool-597'),
        ],
        [
            InlineKeyboardButton('Nalgonda', callback_data='Nalgonda-598'),
            InlineKeyboardButton('Narayanpet', callback_data='Narayanpet-613'),
        ],
        [
            InlineKeyboardButton('Nirmal', callback_data='Nirmal-599'),
            InlineKeyboardButton('Nizamabad', callback_data='Nizamabad-600'),
        ],
        [
            InlineKeyboardButton('Peddapalli', callback_data='Peddapalli-601'),
            InlineKeyboardButton('Rajanna Sircilla', callback_data='Rajanna Sircilla-602'),
        ],
        [
            InlineKeyboardButton('Rangareddy', callback_data='Rangareddy-603'),
            InlineKeyboardButton('Sangareddy', callback_data='Sangareddy-604'),
        ],
        [
            InlineKeyboardButton('Siddipet', callback_data='Siddipet-605'),
            InlineKeyboardButton('Suryapet', callback_data='Suryapet-606'),
        ],
        [
            InlineKeyboardButton('Vikarabad', callback_data='Vikarabad-607'),
            InlineKeyboardButton('Wanaparthy', callback_data='Wanaparthy-608'),
        ],
        [
            InlineKeyboardButton('Warangal(Rural)', callback_data='Warangal(Rural)-609'),
            InlineKeyboardButton('Warangal(Urban)', callback_data='Warangal(Urban)-610'),
        ],
        [
            InlineKeyboardButton('Yadadri Bhuvanagiri', callback_data='Yadadri Bhuvanagiri-611'),
        ]
    ]


    return InlineKeyboardMarkup(keyboard)

def get_district_33() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Dhalai', callback_data='Dhalai-614'),
            InlineKeyboardButton('Gomati', callback_data='Gomati-615'),
        ],
        [
            InlineKeyboardButton('Khowai', callback_data='Khowai-616'),
            InlineKeyboardButton('North Tripura', callback_data='North Tripura-617'),
        ],
        [
            InlineKeyboardButton('Sepahijala', callback_data='Sepahijala-618'),
            InlineKeyboardButton('South Tripura', callback_data='South Tripura-619'),
        ],
        [
            InlineKeyboardButton('Unakoti', callback_data='Unakoti-620'),
            InlineKeyboardButton('West Tripura', callback_data='West Tripura-621'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_34() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Agra', callback_data='Agra-622'),
            InlineKeyboardButton('Aligarh', callback_data='Aligarh-623'),
        ],
        [
            InlineKeyboardButton('Ambedkar Nagar', callback_data='Ambedkar Nagar-625'),
            InlineKeyboardButton('Amethi', callback_data='Amethi-626'),
        ],
        [
            InlineKeyboardButton('Amroha', callback_data='Amroha-627'),
            InlineKeyboardButton('Auraiya', callback_data='Auraiya-628'),
        ],
        [
            InlineKeyboardButton('Ayodhya', callback_data='Ayodhya-646'),
            InlineKeyboardButton('Azamgarh', callback_data='Azamgarh-629'),
        ],
        [
            InlineKeyboardButton('Badaun', callback_data='Badaun-630'),
            InlineKeyboardButton('Baghpat', callback_data='Baghpat-631'),
        ],
        [
            InlineKeyboardButton('Bahraich', callback_data='Bahraich-632'),
            InlineKeyboardButton('Balarampur', callback_data='Balarampur-633'),
        ],
        [
            InlineKeyboardButton('Ballia', callback_data='Ballia-634'),
            InlineKeyboardButton('Banda', callback_data='Banda-635'),
        ],
        [
            InlineKeyboardButton('Barabanki', callback_data='Barabanki-636'),
            InlineKeyboardButton('Bareilly', callback_data='Bareilly-637'),
        ],
        [
            InlineKeyboardButton('Basti', callback_data='Basti-638'),
            InlineKeyboardButton('Bhadohi', callback_data='Bhadohi-687'),
        ],
        [
            InlineKeyboardButton('Bijnour', callback_data='Bijnour-639'),
            InlineKeyboardButton('Bulandshahr', callback_data='Bulandshahr-640'),
        ],
        [
            InlineKeyboardButton('Chandauli', callback_data='Chandauli-641'),
            InlineKeyboardButton('Chitrakoot', callback_data='Chitrakoot-642'),
        ],
        [
            InlineKeyboardButton('Deoria', callback_data='Deoria-643'),
            InlineKeyboardButton('Etah', callback_data='Etah-644'),
        ],
        [
            InlineKeyboardButton('Etawah', callback_data='Etawah-645'),
            InlineKeyboardButton('Farrukhabad', callback_data='Farrukhabad-647'),
        ],
        [
            InlineKeyboardButton('Fatehpur', callback_data='Fatehpur-648'),
            InlineKeyboardButton('Firozabad', callback_data='Firozabad-649'),
        ],
        [
            InlineKeyboardButton('Gautam Buddha Nagar', callback_data='Gautam Buddha Nagar-650'),
            InlineKeyboardButton('Ghaziabad', callback_data='Ghaziabad-651'),
        ],
        [
            InlineKeyboardButton('Ghazipur', callback_data='Ghazipur-652'),
            InlineKeyboardButton('Gonda', callback_data='Gonda-653'),
        ],
        [
            InlineKeyboardButton('Gorakhpur', callback_data='Gorakhpur-654'),
            InlineKeyboardButton('Hamirpur', callback_data='Hamirpur-655'),
        ],
        [
            InlineKeyboardButton('Hapur', callback_data='Hapur-656'),
            InlineKeyboardButton('Hardoi', callback_data='Hardoi-657'),
        ],
        [
            InlineKeyboardButton('Hathras', callback_data='Hathras-658'),
            InlineKeyboardButton('Jalaun', callback_data='Jalaun-659'),
        ],
        [
            InlineKeyboardButton('Jaunpur', callback_data='Jaunpur-660'),
            InlineKeyboardButton('Jhansi', callback_data='Jhansi-661'),
        ],
        [
            InlineKeyboardButton('Kannauj', callback_data='Kannauj-662'),
            InlineKeyboardButton('Kanpur Dehat', callback_data='Kanpur Dehat-663'),
        ],
        [
            InlineKeyboardButton('Kanpur Nagar', callback_data='Kanpur Nagar-664'),
            InlineKeyboardButton('Kasganj', callback_data='Kasganj-665'),
        ],
        [
            InlineKeyboardButton('Kaushambi', callback_data='Kaushambi-666'),
            InlineKeyboardButton('Kushinagar', callback_data='Kushinagar-667'),
        ],
        [
            InlineKeyboardButton('Lakhimpur Kheri', callback_data='Lakhimpur Kheri-668'),
            InlineKeyboardButton('Lalitpur', callback_data='Lalitpur-669'),
        ],
        [
            InlineKeyboardButton('Lucknow', callback_data='Lucknow-670'),
            InlineKeyboardButton('Maharajganj', callback_data='Maharajganj-671'),
        ],
        [
            InlineKeyboardButton('Mahoba', callback_data='Mahoba-672'),
            InlineKeyboardButton('Mainpuri', callback_data='Mainpuri-673'),
        ],
        [
            InlineKeyboardButton('Mathura', callback_data='Mathura-674'),
            InlineKeyboardButton('Mau', callback_data='Mau-675'),
        ],
        [
            InlineKeyboardButton('Meerut', callback_data='Meerut-676'),
            InlineKeyboardButton('Mirzapur', callback_data='Mirzapur-677'),
        ],
        [
            InlineKeyboardButton('Moradabad', callback_data='Moradabad-678'),
            InlineKeyboardButton('Muzaffarnagar', callback_data='Muzaffarnagar-679'),
        ],
        [
            InlineKeyboardButton('Pilibhit', callback_data='Pilibhit-680'),
            InlineKeyboardButton('Pratapgarh', callback_data='Pratapgarh-682'),
        ],
        [
            InlineKeyboardButton('Prayagraj', callback_data='Prayagraj-624'),
            InlineKeyboardButton('Raebareli', callback_data='Raebareli-681'),
        ],
        [
            InlineKeyboardButton('Rampur', callback_data='Rampur-683'),
            InlineKeyboardButton('Saharanpur', callback_data='Saharanpur-684'),
        ],
        [
            InlineKeyboardButton('Sambhal', callback_data='Sambhal-685'),
            InlineKeyboardButton('Sant Kabir Nagar', callback_data='Sant Kabir Nagar-686'),
        ],
        [
            InlineKeyboardButton('Shahjahanpur', callback_data='Shahjahanpur-688'),
            InlineKeyboardButton('Shamli', callback_data='Shamli-689'),
        ],
        [
            InlineKeyboardButton('Shravasti', callback_data='Shravasti-690'),
            InlineKeyboardButton('Siddharthnagar', callback_data='Siddharthnagar-691'),
        ],
        [
            InlineKeyboardButton('Sitapur', callback_data='Sitapur-692'),
            InlineKeyboardButton('Sonbhadra', callback_data='Sonbhadra-693'),
        ],
        [
            InlineKeyboardButton('Sultanpur', callback_data='Sultanpur-694'),
            InlineKeyboardButton('Unnao', callback_data='Unnao-695'),
        ],
        [
            InlineKeyboardButton('Varanasi', callback_data='Varanasi-696'),
        ]
    ]


    return InlineKeyboardMarkup(keyboard)

def get_district_35() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Almora', callback_data='Almora-704'),
            InlineKeyboardButton('Bageshwar', callback_data='Bageshwar-707'),
        ],
        [
            InlineKeyboardButton('Chamoli', callback_data='Chamoli-699'),
            InlineKeyboardButton('Champawat', callback_data='Champawat-708'),
        ],
        [
            InlineKeyboardButton('Dehradun', callback_data='Dehradun-697'),
            InlineKeyboardButton('Haridwar', callback_data='Haridwar-702'),
        ],
        [
            InlineKeyboardButton('Nainital', callback_data='Nainital-709'),
            InlineKeyboardButton('Pauri Garhwal', callback_data='Pauri Garhwal-698'),
        ],
        [
            InlineKeyboardButton('Pithoragarh', callback_data='Pithoragarh-706'),
            InlineKeyboardButton('Rudraprayag', callback_data='Rudraprayag-700'),
        ],
        [
            InlineKeyboardButton('Tehri Garhwal', callback_data='Tehri Garhwal-701'),
            InlineKeyboardButton('Udham Singh Nagar', callback_data='Udham Singh Nagar-705'),
        ],
        [
            InlineKeyboardButton('Uttarkashi', callback_data='Uttarkashi-703'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_36() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Alipurduar District', callback_data='Alipurduar District-710'),
            InlineKeyboardButton('Bankura', callback_data='Bankura-711'),
        ],
        [
            InlineKeyboardButton('Basirhat HD (North 24 Parganas)', callback_data='Basirhat HD (North 24 Parganas)-712'),
            InlineKeyboardButton('Birbhum', callback_data='Birbhum-713'),
        ],
        [
            InlineKeyboardButton('Bishnupur HD (Bankura)', callback_data='Bishnupur HD (Bankura)-714'),
            InlineKeyboardButton('Cooch Behar', callback_data='Cooch Behar-715'),
        ],
        [
            InlineKeyboardButton('COOCHBEHAR', callback_data='COOCHBEHAR-783'),
            InlineKeyboardButton('Dakshin Dinajpur', callback_data='Dakshin Dinajpur-716'),
        ],
        [
            InlineKeyboardButton('Darjeeling', callback_data='Darjeeling-717'),
            InlineKeyboardButton('Diamond Harbor HD (S 24 Parganas)', callback_data='Diamond Harbor HD (S 24 Parganas)-718'),
        ],
        [
            InlineKeyboardButton('East Bardhaman', callback_data='East Bardhaman-719'),
            InlineKeyboardButton('Hoogly', callback_data='Hoogly-720'),
        ],
        [
            InlineKeyboardButton('Howrah', callback_data='Howrah-721'),
            InlineKeyboardButton('Jalpaiguri', callback_data='Jalpaiguri-722'),
        ],
        [
            InlineKeyboardButton('Jhargram', callback_data='Jhargram-723'),
            InlineKeyboardButton('Kalimpong', callback_data='Kalimpong-724'),
        ],
        [
            InlineKeyboardButton('Kolkata', callback_data='Kolkata-725'),
            InlineKeyboardButton('Malda', callback_data='Malda-726'),
        ],
        [
            InlineKeyboardButton('Murshidabad', callback_data='Murshidabad-727'),
            InlineKeyboardButton('Nadia', callback_data='Nadia-728'),
        ],
        [
            InlineKeyboardButton('Nandigram HD (East Medinipore)', callback_data='Nandigram HD (East Medinipore)-729'),
            InlineKeyboardButton('North 24 Parganas', callback_data='North 24 Parganas-730'),
        ],
        [
            InlineKeyboardButton('Paschim Medinipore', callback_data='Paschim Medinipore-731'),
            InlineKeyboardButton('Purba Medinipore', callback_data='Purba Medinipore-732'),
        ],
        [
            InlineKeyboardButton('Purulia', callback_data='Purulia-733'),
            InlineKeyboardButton('Rampurhat HD (Birbhum)', callback_data='Rampurhat HD (Birbhum)-734'),
        ],
        [
            InlineKeyboardButton('South 24 Parganas', callback_data='South 24 Parganas-735'),
            InlineKeyboardButton('Uttar Dinajpur', callback_data='Uttar Dinajpur-736'),
        ],
        [
            InlineKeyboardButton('West Bardhaman', callback_data='West Bardhaman-737'),
        ]

    ]

    return InlineKeyboardMarkup(keyboard)

def get_district_37() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Daman', callback_data='Daman-138'),
            InlineKeyboardButton('Diu', callback_data='Diu-139'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)