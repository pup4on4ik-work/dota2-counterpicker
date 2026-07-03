from tkinter import *
from tkinter import scrolledtext

import os

# Имена файлов для хранения
SETTINGS_FILE = "settings.txt"

def load_settings():
    """Загружает героев из файла или возвращает значения по умолчанию"""
    default_m1 = "tiny, tinker, timbersaw, ursa, kez, rubick, void_spirit, invoker"
    default_m2 = "ancient_apparition, jakiro, mirana, disruptor, vengeful_spirit"
    
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                lines = f.readlines()
                if len(lines) >= 2:
                    return lines[0].strip(), lines[1].strip()
        except:
            pass # Если файл поврежден, вернем дефолт
    return default_m1, default_m2

def save_settings_to_file(m1, m2):
    """Записывает героев в текстовый файл"""
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        f.write(f"{m1}\n{m2}")

window = Tk()
window.geometry('520x620')
window.title('Dota 2 Counterpicker')
window.configure(bg='#121212')




#kod

import time
from time import sleep as sleep
import random
from random import randint as rnt


#палитра сука

bg_main = '#121212'
bg_input = '#1e1e1e'      
text_main = '#ffffff'     
text_res = '#cfcfcf'      
accent_blue = '#0078d4'   

#dannie

m1_heroes_str, m2_heroes_str = load_settings()

#full heroes kontrpicks


heroes_db = {
    "abaddon": ['slark', 'ancient_apparition', 'outworld_destroyer', 'axe', 'doom', 'phantom_lancer'],
    "alchemist": ['slardar', 'ancient_apparition', 'necrophos', 'lifestealer', 'ursa', 'huskar'],
    "anti_mage": ['meepo', 'phantom_assassin', 'templar_assassin', 'huskar', 'slardar', 'riki'],
    "axe": ['ursa', 'lifestealer', 'venomancer', 'viper', 'doom', 'outworld_destroyer'],
    "bristleback": ['viper', 'slardar', 'legion_commander', 'necrophos', 'faceless_void', 'anti_mage'],
    "crystal_maiden": ['clockwerk', 'nyx_assassin', 'tusk', 'bounty_hunter', 'earth_spirit', 'spectre'],
    "drow_ranger": ['phantom_assassin', 'spectre', 'riki', 'slark', 'axe', 'centaur_warrunner'],
    "invoker": ['broodmother', 'templar_assassin', 'kunkka', 'phantom_lancer', 'anti_mage', 'silencer'],
    "juggernaut": ['ursa', 'slardar', 'axe', 'legion_commander', 'phantom_assassin', 'void_spirit'],
    "legion_commander": ['ursa', 'troll_warlord', 'monkey_king', 'abaddon', 'dazzle', 'winter_wyvern'],
    "lifestealer": ['slardar', 'razor', 'bane', 'ursa', 'beastmaster', 'troll_warlord'],
    "phantom_assassin": ['morphling', 'axe', 'razor', 'tinker', 'bristleback', 'centaur_warrunner'],
    "pudge": ['lifestealer', 'slardar', 'ursa', 'timbersaw', 'monkey_king', 'enigma'],
    "slark": ['bloodseeker', 'leshrac', 'disruptor', 'axe', 'legion_commander', 'puck'],
    "sniper": ['spectre', 'phantom_assassin', 'storm_spirit', 'bounty_hunter', 'clockwerk', 'spirit_breaker'],
    "spirit_breaker": ['underlord', 'ember_spirit', 'outworld_destroyer', 'nyx_assassin', 'grimstroke', 'clinkz'],
    "wraith_king": ['anti_mage', 'phantom_lancer', 'slark', 'invoker', 'lion', 'weaver'],
    "faceless_void": ['pudge', 'shadow_demon', 'winter_wyvern', 'axe', 'razor', 'omniknight'],
    "spectre": ['lifestealer', 'necrophos', 'slark', 'undying', 'viper', 'weaver'],
    "morphling": ['ancient_apparition', 'anti_mage', 'outworld_destroyer', 'axe', 'phantom_lancer', 'lion'],
    "mars": ['lifestealer', 'viper', 'timbersaw', 'necrophos', 'slark', 'phoenix'],
    "monkey_king": ['timbersaw', 'batrider', 'beastmaster', 'spirit_breaker', 'windranger', 'pudge'],
    "void_spirit": ['meepo', 'night_stalker', 'silencer', 'puck', 'doom', 'skywrath_mage'],
    "muerta": ['anti_mage', 'phantom_assassin', 'spectre', 'juggernaut', 'slark', 'lina'],
    "tidehunter": ['ursa', 'slark', 'lifestealer', 'necrophos', 'outworld_destroyer', 'monkey_king'],
    "dazzle": ['axe', 'ancient_apparition', 'silencer', 'night_stalker', 'doom', 'legion_commander'],
    "bloodseeker": ['troll_warlord', 'medusa', 'morphling', 'pudge', 'terrorblade', 'monkey_king'],
    "huskar": ['ancient_apparition', 'necrophos', 'viper', 'chaos_knight', 'ursa', 'lifestealer'],
    "meepo": ['elder_titan', 'leshrac', 'winter_wyvern', 'sven', 'axe', 'pangolier'],
    "outworld_destroyer": ['nyx_assassin', 'sniper', 'pugna', 'templar_assassin', 'lone_druid', 'droll_warlord'],
    "templar_assassin": ['venomancer', 'viper', 'batrider', 'jakiro', 'pudge', 'alchemist'],
    "windranger": ['centaur_warrunner', 'spectre', 'axe', 'mars', 'bristleback', 'tinker'],
    "phantom_lancer": ['leshrac', 'earthshaker', 'sven', 'sand_king', 'mjollnir_users', 'legion_commander'],
    "necrophos": ['anti_mage', 'silencer', 'viper', 'huskar', 'medusa', 'drizzlehunter'],
    "medusa": ['anti_mage', 'diffusal_blade_users', 'nyx_assassin', 'slark', 'invoker', 'outworld_destroyer'],
    "earthshaker": ['viper', 'lifestealer', 'clockwerk', 'spectre', 'silencer', 'timbersaw'],
    "sven": ['troll_warlord', 'ursa', 'lifestealer', 'winter_wyvern', 'axe', 'razor'],
    "kunkka": ['lifestealer', 'ursa', 'outworld_destroyer', 'timbersaw', 'monkey_king', 'slark'],
    "beastmaster": ['winter_wyvern', 'timbersaw', 'crystal_maiden', 'keeper_of_the_light', 'lich', 'enigma'],
    "dragon_knight": ['lifestealer', 'ursa', 'slark', 'timbersaw', 'outworld_destroyer', 'razor'],
    "clockwerk": ['lifestealer', 'ursa', 'monkey_king', 'phantom_lancer', 'anti_mage', 'juggernaut'],
    "omniknight": ['shadow_demon', 'oracle', 'invoker', 'brewmaster', 'null_ifier_users', 'enchantress'],
    "brewmaster": ['anti_mage', 'silencer', 'night_stalker', 'skywrath_mage', 'death_prophet', 'doom'],
    "centaur_warrunner": ['lifestealer', 'ursa', 'slark', 'timbersaw', 'necrophos', 'monkey_king'],
    "magnus": ['ursa', 'slark', 'lifestealer', 'enigma', 'batrider', 'tidehunter'],
    "tusk": ['ursa', 'slark', 'lifestealer', 'phantom_lancer', 'meepo', 'naga_siren'],
    "underlord": ['ursa', 'slark', 'lifestealer', 'monkey_king', 'timbersaw', 'necrophos'],
    "phoenix": ['ursa', 'juggernaut', 'lifestealer', 'snapfire', 'clinkz', 'silencer'],
    "earth_spirit": ['anti_mage', 'silencer', 'night_stalker', 'skywrath_mage', 'doom', 'puck'],
    "ember_spirit": ['slardar', 'axe', 'legion_commander', 'faceless_void', 'silencer', 'storm_spirit'],
    "arc_warden": ['meepo', 'phantom_lancer', 'naga_siren', 'spectre', 'slark', 'anti_mage'],
    "snapfire": ['lifestealer', 'ursa', 'slark', 'faceless_void', 'juggernaut', 'weaver'],
    "dawnbreaker": ['ursa', 'lifestealer', 'slark', 'necrophos', 'beastmaster', 'enigma'],
    "marci": ['axe', 'legion_commander', 'winter_wyvern', 'enigma', 'faceless_void', 'bane'],
    "primal_beast": ['lifestealer', 'ursa', 'slark', 'necrophos', 'viper', 'timbersaw'],
    "terrorblade": ['zeus', 'tinker', 'leshrac', 'necrophos', 'timbersaw', 'axe'],
    "naga_siren": ['leshrac', 'earthshaker', 'sand_king', 'sven', 'axe', 'mjollnir_users'],
    "slardar": ['naga_siren', 'phantom_lancer', 'ursa', 'lifestealer', 'abaddon', 'tidehunter'],
    "sand_king": ['lifestealer', 'ursa', 'juggernaut', 'slark', 'anti_mage', 'viper'],
    "enigma": ['silencer', 'rubick', 'night_stalker', 'warlock', 'vengeful_spirit', 'clockwerk'],
    "venomancer": ['juggernaut', 'lifestealer', 'oracle', 'abaddon', 'huskar', 'phantom_lancer'],
    "viper": ['phantom_lancer', 'naga_siren', 'chaos_knight', 'terrorblade', 'anti_mage', 'juggernaut'],
    "razor": ['weaver', 'clinkz', 'sniper', 'outworld_destroyer', 'anti_mage', 'phantom_lancer'],
    "leshrac": ['anti_mage', 'huskar', 'nyx_assassin', 'sniper', 'pugna', 'viper'],
    "death_prophet": ['ancient_apparition', 'sniper', 'anti_mage', 'huskar', 'medusa', 'viper'],
    "pugna": ['anti_mage', 'nyx_assassin', 'sniper', 'viper', 'huskar', 'silencer'],
    "enchantress": ['phantom_assassin', 'ursa', 'juggernaut', 'lifestealer', 'broodmother', 'weaver'],
    "chen": ['earthshaker', 'sven', 'clinkz', 'sand_king', 'lina', 'crystal_maiden'],
    "batrider": ['abaddon', 'oracle', 'legion_commander', 'vengeful_spirit', 'slark', 'weaver'],
    "dark_seer": ['oracle', 'anti_mage', 'ember_spirit', 'juggernaut', 'slark', 'vengeful_spirit'],
    "dark_willow": ['puck', 'anti_mage', 'juggernaut', 'lifestealer', 'night_stalker', 'silencer'],
    "hoodwink": ['spirit_breaker', 'storm_spirit', 'spectre', 'clockwerk', 'nyx_assassin', 'puck'],
    "pangolier": ['bloodseeker', 'axe', 'faceless_void', 'legion_commander', 'grimstroke', 'doom'],
    "grimstroke": ['anti_mage', 'phantom_assassin', 'weaver', 'clinkz', 'slark', 'huskar'],
    "oracle": ['axe', 'ancient_apparition', 'silencer', 'night_stalker', 'doom', 'phantom_assassin'],
    "winter_wyvern": ['anti_mage', 'silencer', 'night_stalker', 'skywrath_mage', 'timbersaw', 'pudge'],
    "techies": ['lifestealer', 'juggernaut', 'anti_mage', 'wraith_king', 'phantom_lancer', 'night_stalker'],
    "ringmaster": ['anti_mage', 'silencer', 'night_stalker', 'nyx_assassin', 'puck', 'doom'],
    "elder_titan": ['slark', 'ursa', 'lifestealer', 'weaver', 'clinkz', 'monkey_king'],
    "doom": ['wraith_king', 'medusa', 'meepo', 'lifestealer', 'linkens_sphere_users', 'lotus_orb_users'],
    "chaos_knight": ['earthshaker', 'sven', 'phantom_lancer', 'medusa', 'enigma', 'sand_king'],
    "lycan": ['winter_wyvern', 'axe', 'bristleback', 'sven', 'earthshaker', 'tidehunter'],
    "night_stalker": ['bristleback', 'underlord', 'tidehunter', 'axe', 'dragon_knight', 'meepo'],
    "ogre_magi": ['chaos_knight', 'lifestealer', 'phantom_lancer', 'anti_mage', 'meepo', 'naga_siren'],
    "treant_protector": ['timbersaw', 'batrider', 'phoenix', 'lina', 'ember_spirit', 'jakiro'],
    "undying": ['ursa', 'clinkz', 'weaver', 'sniper', 'gyrocopter', 'troll_warlord'],
    "bounty_hunter": ['slardar', 'spirit_breaker', 'bloodseeker', 'necrophos', 'axe', 'legion_commander'],
    "broodmother": ['earthshaker', 'legion_commander', 'kunkka', 'axe', 'sven', 'sand_king'],
    "clinkz": ['slardar', 'bounty_hunter', 'bloodseeker', 'axe', 'legion_commander', 'phantom_lancer'],
    "gyrocopter": ['juggernaut', 'lifestealer', 'anti_mage', 'huskar', 'clockwerk', 'spectre'],
    "lone_druid": ['lifestealer', 'ursa', 'winter_wyvern', 'weaver', 'monkey_king', 'slark'],
    "luna": ['phantom_assassin', 'spectre', 'slark', 'juggernaut', 'lifestealer', 'huskar'],
    "riki": ['slardar', 'bounty_hunter', 'bloodseeker', 'axe', 'legion_commander', 'faceless_void'],
    "shadow_fiend": ['templar_assassin', 'puck', 'storm_spirit', 'viper', 'nyx_assassin', 'batrider'],
    "troll_warlord": ['axe', 'winter_wyvern', 'bane', 'razor', 'outworld_destroyer', 'pudge'],
    "weaver": ['faceless_void', 'axe', 'legion_commander', 'bloodseeker', 'slardar', 'spirit_breaker'],
    "keeper_of_the_light": ['spirit_breaker', 'storm_spirit', 'spectre', 'clockwerk', 'nyx_assassin', 'anti_mage'],
    "lich": ['anti_mage', 'silencer', 'night_stalker', 'puck', 'lifestealer', 'juggernaut'],
    "lina": ['phantom_assassin', 'spectre', 'anti_mage', 'storm_spirit', 'nyx_assassin', 'spirit_breaker'],
    "lion": ['anti_mage', 'phantom_lancer', 'naga_siren', 'lifestealer', 'juggernaut', 'abaddon'],
    "puck": ['templar_assassin', 'nyx_assassin', 'night_stalker', 'anti_mage', 'silencer', 'skywrath_mage'],
    "queen_of_pain": ['puck', 'night_stalker', 'anti_mage', 'silencer', 'nyx_assassin', 'skywrath_mage'],
    "rubick": ['anti_mage', 'phantom_assassin', 'clinkz', 'weaver', 'slark', 'riki'],
    "shadow_demon": ['anti_mage', 'phantom_assassin', 'clinkz', 'weaver', 'slark', 'phantom_lancer'],
    "shadow_shaman": ['anti_mage', 'lifestealer', 'juggernaut', 'slark', 'abaddon', 'oracle'],
    "silencer": ['phantom_assassin', 'huskar', 'ursa', 'lifestealer', 'juggernaut', 'anti_mage'],
    "skywrath_mage": ['anti_mage', 'nyx_assassin', 'pugna', 'huskar', 'lifestealer', 'juggernaut'],
    "storm_spirit": ['anti_mage', 'nyx_assassin', 'silencer', 'night_stalker', 'meepo', 'skywrath_mage'],
    "warlock": ['weaver', 'clinkz', 'anti_mage', 'juggernaut', 'lifestealer', 'slark'],
    "witch_doctor": ['clinkz', 'weaver', 'phantom_assassin', 'anti_mage', 'juggernaut', 'lifestealer'],
    "zeus": ['anti_mage', 'phantom_assassin', 'spectre', 'huskar', 'templar_assassin', 'viper'],
    "bane": ['phantom_lancer', 'naga_siren', 'chaos_knight', 'abaddon', 'lotus_orb_users', 'tidehunter'],
    "io": ['ancient_apparition', 'disruptor', 'silencer', 'night_stalker', 'enigma', 'axe'],
    "natures_prophet": ['spirit_breaker', 'spectre', 'storm_spirit', 'clockwerk', 'anti_mage', 'puck'],
    "nyx_assassin": ['slardar', 'bounty_hunter', 'juggernaut', 'lifestealer', 'abaddon', 'tidehunter'],
    "visage": ['phantom_lancer', 'naga_siren', 'axe', 'bristleback', 'tidehunter', 'crimson_guard_users'],
    "tiny": ['lifestealer', 'necrophos', 'slark', 'viper', 'axe', 'venomancer'],
    "tinker": ['clockwerk', 'nyx_assassin', 'spectre', 'night_stalker', 'anti_mage', 'storm_spirit'],
    "timbersaw": ['ursa', 'necrophos', 'viper', 'silencer', 'ancient_apparition', 'outworld_destroyer'],
    "ursa": ['venomancer', 'viper', 'razor', 'windranger', 'necrophos', 'shadow_demon'],
    "kez": ['axe', 'legion_commander', 'faceless_void', 'doom', 'winter_wyvern', 'bane'],
    "ancient_apparition": ['weaver', 'clinkz', 'phantom_assassin', 'anti_mage', 'slark', 'riki'],
    "mirana": ['night_stalker', 'spirit_breaker', 'bounty_hunter', 'slardar', 'clockwerk', 'spectre'],
    "disruptor": ['lifestealer', 'juggernaut', 'anti_mage', 'puck', 'silencer', 'night_stalker'],
    "jakiro": ['lifestealer', 'juggernaut', 'anti_mage', 'oracle', 'abaddon', 'viper'],
    "vengeful_spirit": ['phantom_lancer', 'anti_mage', 'naga_siren', 'chaos_knight', 'terrorblade', 'juggernaut']
}


#spiski
what_c=[]
v=[]
all_c=[]



#proverka

def proverka_all():
    errors=[]
    user_input=clean_input(osnov.get()).split()
    for error_word in user_input:
        if error_word not in heroes_db and error_word!='':
            errors.append(error_word)
    return errors
            
#help {}            

def clean_input(text):
    return text.replace('{', '').replace('}', '').replace(',', ' ').lower().strip()

#kod osnov

def delete():
    listkontrpicks.delete(0.0,END)
    osnov.delete(0,END)

def deleteentry():
    osnov.delete(0,END)


def process_hero(kontrpicks,name_hero,hero_list):
    clean_code = clean_input(osnov.get())
    for k in kontrpicks:
        if k in clean_code:
            if kontrpicks.index(k)==0: hero_list.append((k+'(100%)','critical'))
            elif kontrpicks.index(k) in [1,2]: hero_list.append((k+'(90%)','medium'))
            elif kontrpicks.index(k) in [3,4]: hero_list.append((k+'(80%)','warning'))
            elif kontrpicks.index(k) in [5,6]: hero_list.append((k+'(70%)','safe'))
    if hero_list==v:
        listkontrpicks.insert(END,f'Контрпики {name_hero}: нет\n','safe')
        what_c.append(name_hero)
        return False
    else:
        listkontrpicks.insert(END,f'Контрпики {name_hero}: ','neutral')
        for item, tag in hero_list:
            listkontrpicks.insert(END, item + " ", tag)
        listkontrpicks.insert(END,'\n')
        return True
#Meins kod
def Mein1():
    listkontrpicks.insert(END, '...\n')
    what_c.clear()
    
    heroes_to_check = [h.strip().lower() for h in m1_heroes_str.split(',') if h.strip()]
    for h_name in heroes_to_check:
        if h_name in heroes_db:
            c_hero_list=[]
            process_hero(heroes_db[h_name],h_name,c_hero_list)
        else:
            listkontrpicks.insert(END, f"Герой {h_name} не найден в базе.\n", 'error_style')
    
    if what_c!=v:
        listkontrpicks.insert(END,f'Герои у которых нет контрпиков в этой игре:\n{" ".join(what_c)}\n')
    else:
        listkontrpicks.insert(END,'В этой игре есть контрпики всех ваших сигнатурок\n')

    errors_process=proverka_all()
    errors_pretty=' '.join(errors_process)
    
    if errors_process:
        listkontrpicks.insert(END,f"Герои {errors_pretty} не найдены в базе.\n",'error_style')

def Mein2():
    listkontrpicks.insert(END, '...\n')
    what_c.clear()
    
    heroes_to_check = [h.strip().lower() for h in m2_heroes_str.split(',') if h.strip()]
    for h_name in heroes_to_check:
        if h_name in heroes_db:
            c_hero_list=[]
            process_hero(heroes_db[h_name],h_name,c_hero_list)
        else:
            listkontrpicks.insert(END, f"Герой {h_name} не найден в базе.\n", 'error_style')
    
    if what_c!=v:
        listkontrpicks.insert(END,f'Герои у которых нет контрпиков в этой игре:\n{" ".join(what_c)}\n')
    else:
        listkontrpicks.insert(END,'В этой игре есть контрпики всех ваших сигнатурок\n')

    errors_process=proverka_all()
    errors_pretty=' '.join(errors_process)
    
    if errors_process:
        listkontrpicks.insert(END,f"Герои {errors_pretty} не найдены в базе.\n",'error_style')
   
def open_settings():
    settings_win = Toplevel(window)
    settings_win.title("Настройка героев")
    settings_win.geometry("400x300")
    settings_win.configure(bg=bg_main)

    Label(settings_win, text="ГЕРОИ МЕЙН 1 (через запятую):", bg=bg_main, fg='#888888', font='Arial 8 bold').pack(pady=(20, 5))
    entry_m1 = Entry(settings_win, width=40, bg=bg_input, fg=text_main, font='Arial 11', relief=FLAT, bd=8)
    entry_m1.insert(0, m1_heroes_str)
    entry_m1.pack()

    Label(settings_win, text="ГЕРОИ МЕЙН 2 (через запятую):", bg=bg_main, fg='#888888', font='Arial 8 bold').pack(pady=(20, 5))
    entry_m2 = Entry(settings_win, width=40, bg=bg_input, fg=text_main, font='Arial 11', relief=FLAT, bd=8)
    entry_m2.insert(0, m2_heroes_str)
    entry_m2.pack()

    def save_and_close():
        global m1_heroes_str, m2_heroes_str
        m1_heroes_str = entry_m1.get()
        m2_heroes_str = entry_m2.get()
        
        # СОХРАНЯЕМ В ФАЙЛ
        save_settings_to_file(m1_heroes_str, m2_heroes_str)
        
        settings_win.destroy()

    # Кнопка сохранения
    Button(settings_win, text='СОХРАНИТЬ', bg=accent_blue, fg='white', 
           font='Arial 9 bold', width=15, height=2, command=save_and_close, cursor="hand2", relief=FLAT).pack(pady=30)    



# Поле ввода
Label(window, text="КАНДИДАТЫ НА КОНТРПИК", bg=bg_main, fg='#888888', font='Arial 9 bold').pack(pady=(20, 0))

osnov = Entry(window, width=40, justify=CENTER, 
              bg=bg_input, 
              fg=text_main, 
              insertbackground='white', # Цвет мигающей палочки
              font='Arial 13', 
              relief=FLAT, bd=12)
osnov.pack(pady=10)

# Кнопки
btn_frame = Frame(window, bg=bg_main)
btn_frame.pack(pady=10)

button1 = Button(btn_frame, text='МЕЙН 1', relief=FLAT, bg=accent_blue, fg='white', 
                 font='Arial 9 bold', width=15, height=2, command=Mein1, cursor="hand2")
button1.grid(row=0, column=0, padx=5)

button3 = Button(btn_frame, text='СБРОС', relief=FLAT, bg='#333333', fg='#ff4d4d', 
                 font='Arial 9 bold', width=10, height=2, command=delete, cursor="hand2")
button3.grid(row=0, column=1, padx=5)

button2 = Button(btn_frame, text='МЕЙН 2', relief=FLAT, bg=accent_blue, fg='white', 
                 font='Arial 9 bold', width=15, height=2, command=Mein2, cursor="hand2")
button2.grid(row=0, column=2, padx=5)

Button(window, text='НАСТРОЙКИ', bg='#333333', fg='#cfcfcf', 
       font='Arial 8 bold', command=open_settings, relief=FLAT, cursor="hand2").pack(side=BOTTOM, pady=10)


# Поле вывода
listkontrpicks = Text(window, font='Consolas 11', width=55, height=20, 
                      fg=text_res, 
                      bg=bg_input, 
                      relief=FLAT, bd=15)
listkontrpicks.pack(padx=20, pady=10)

listkontrpicks.tag_config("error_style", foreground="#ff4d4d")
listkontrpicks.tag_config("critical", foreground="#ff4d4d")
listkontrpicks.tag_config("medium", foreground="#ffa500")
listkontrpicks.tag_config("warning", foreground="#ffff00")
listkontrpicks.tag_config("safe", foreground="#00ff41")
listkontrpicks.tag_config("neutral", foreground="#a9b1d6")


window.mainloop()
