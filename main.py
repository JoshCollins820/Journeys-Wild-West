## JOURNEYS WILD WEST
## v0.5
## Developed by: Josh Collins
## --------------------------

# Modules
import pygame
import random
import sys
import pickle

# SimpleGUI Module
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# window resolution
width = 600  # 1280
height = 600  # 800


# pygame initialization
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(10)  # default is 8
clock = pygame.time.Clock()
random.seed()

# window properties
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("JOURNEYS: WILD WEST")
pygame.display.set_icon(pygame.image.load("assets/icon/window_icon.png"))
collapse = True
version = "0.5"

# values and statements
if collapse:
    # MAKE SURE TO ALSO CHANGE VALUES IN RESETVALUES METHOD -------------------------------------------------------
    # vals
    playerHP = 100
    moneyCount = 0
    revRoundsMag = 6
    revRoundsTotal = 24
    revolverDamage = 20
    revolverFireRate = 12
    revolverReloadSpeed = 500
    sniperRoundsMag = 1
    sniperRoundsTotal = 3
    sniperDamage = 100
    sawedOffRoundsMag = 2
    buckRoundsTotal = 6
    sawedOffDamage = 50
    hpPotionCount = 0
    drinkTime = 250
    beerRegenRate = 30
    beerRegenAmount = 50
    healQueue = 0
    score = 0
    highscore = 0
    masterVolumeStored = 0
    musicVolumeStored = 0
    banditCount = 0
    snakeCount = 0
    wave = 0
    waveIntermissionLength = 1500
    venom_ticks_remaining = 0
    tumweedReset = -3000
    tumweedSpawn = 2000
    lastActiveSlot = 1

    # speed
    speedMove = 50
    cloudMove = 8
    cloudAuto = 0.2
    tumbleAuto = 15
    banMove = 8

    # x,y cords
    cloud1x = 100
    cloud2x = 600
    tumweed1x = 700
    store1x = 700
    store2x = 1400
    cactusx = 450
    cooldown_sweat_y = 252
    hp_gain1_y = 250
    hp_gain2_y = 235
    hp_gain3_y = 262
    activeSlotx1 = -50
    activeSlotx2 = -50
    bulletx = 330
    scopeWalk = 0

    # statements
    devMode = True
    godMode = False
    invincibility = False
    invisible = False
    displayHUD = True
    moveAbility = True
    banMoveAbility = True
    interactText = False
    buyText = False
    sitting = False
    standing = True
    walkingRight = False
    walkingLeft = False
    walkingBoth = False
    rolling = False
    poisoned = False
    moneyPick = False
    moneyPickText = False
    showMoney = True
    insufFundsText = False
    purchasedText = False
    lookingLeft = False
    lookingRight = True
    hotbarSlot1 = False
    hotbarSlot2 = False
    hotbarSlot3 = False
    hotbarSlot4 = False
    hotbarSlot5 = False
    hotbarSlot6 = False
    startGame = False
    reloadUI = False
    outAmmoUI = False
    revolverOutMag = False
    sniperOutMag = False
    sawedOffOutMag = False
    revolverOutAmmo = False
    sniperOutAmmo = False
    sawedOffOutAmmo = False
    dead = False
    scopeScreen = False
    insideShop = False
    insideSaloon = False
    ownSniperRifle = False
    ownSawedOff = False
    catalog = False
    catalogPage1 = False
    catalogPage2 = False
    catalogPage3 = False
    playerIdle = True
    playerWalk = False
    playerHolster = False
    playerLegsIdle = True
    playerShoot = False
    playerDrink = False
    playerSniper = False
    playerGrab = False
    readyToFireRevolver = True
    playButtonHover = False
    playButtonClicked = False
    restartButtonHover = False
    restartButtonClicked = False
    mainMenuButtonHover = False
    mainMenuButtonClicked = False
    pause = False
    resumeButtonHover = False
    resumeButtonClicked = False
    settingsButtonHover = False
    settingsButtonClicked = False
    mainMenu2ButtonHover = False
    mainMenu2ButtonClicked = False
    confirmYesButtonHover = False
    confirmYesButtonClicked = False
    confirmNoButtonHover = False
    confirmNoButtonClicked = False
    confirmationBox = False
    settings = False
    settingsDoneButtonHover = False
    settingsDoneButtonClicked = False
    masterLeftButtonHover = False
    masterLeftButtonClicked = False
    masterRightButtonHover = False
    masterRightButtonClicked = False
    musicLeftButtonHover = False
    musicLeftButtonClicked = False
    musicRightButtonHover = False
    musicRightButtonClicked = False
    musicIconButtonClicked = False
    musicIconButtonHover = False
    masterIconButtonClicked = False
    masterIconButtonHover = False
    exitButtonHover = False
    masterVolumeMuted = False
    musicVolumeMuted = False
    playerRoll1Right = False
    playerRoll2Right = False
    playerRoll3Right = False
    playerRoll1Left = False
    playerRoll2Left = False
    playerRoll3Left = False
    rollReady = True
    looting = False
    showMoneyGainedText = False
    healing = False
    showWave = False
    reloading = False
    buyHoverP1_1 = False
    buyHoverP1_2 = False
    buyHoverP1_3 = False
    buyHoverP2_1 = False
    buyHoverP2_2 = False
    buyHoverP2_3 = False
    buyHoverP2_4 = False
    demoMode = False
    if demoMode == True:
        ownSniperRifle = True
        ownSawedOff = False
        sniperRoundsTotal = 8
        buckRoundsTotal = 16
        revRoundsTotal = 24
        hpPotionCount = 2
        moneyCount = 100

    # MAKE SURE TO ALSO CHANGE VALUES IN RESETVALUES METHOD -------------------------------------------------------

# audio
if collapse:
    masterVolume = 1  # (0-1)
    musicVolume = 0  # (0-1)
    step = pygame.mixer.Sound('assets/sounds/step.wav')
    woodstep = pygame.mixer.Sound('assets/sounds/woodstep.wav')
    intro = pygame.mixer.Sound('assets/sounds/start_music.wav')
    button = pygame.mixer.Sound('assets/sounds/button.wav')
    griprevolver = pygame.mixer.Sound('assets/sounds/griprevolver.wav')
    shot = pygame.mixer.Sound('assets/sounds/shot.wav')
    empty = pygame.mixer.Sound('assets/sounds/empty.wav')
    reload = pygame.mixer.Sound('assets/sounds/reload.wav')
    revolverspin = pygame.mixer.Sound('assets/sounds/revolverspin.wav')
    death = pygame.mixer.Sound('assets/sounds/death.wav')
    playerhit = pygame.mixer.Sound('assets/sounds/playerhit.wav')
    banpain = pygame.mixer.Sound('assets/sounds/banpain.wav')
    snipershot = pygame.mixer.Sound('assets/sounds/snipershot.wav')
    heartbeat = pygame.mixer.Sound('assets/sounds/heartbeat.wav')
    breath = pygame.mixer.Sound('assets/sounds/breath.wav')
    intromusic = pygame.mixer.Sound('assets/sounds/menu_music.wav')
    door = pygame.mixer.Sound('assets/sounds/door.wav')
    openbook = pygame.mixer.Sound('assets/sounds/openbook.wav')
    turnpage = pygame.mixer.Sound('assets/sounds/turnpage.wav')
    cashregister = pygame.mixer.Sound('assets/sounds/cashregister.wav')
    error = pygame.mixer.Sound('assets/sounds/error.wav')
    music = pygame.mixer.Sound('assets/sounds/bg_music.wav')
    potion = pygame.mixer.Sound('assets/sounds/beer_drink.wav')
    sniper_reload = pygame.mixer.Sound('assets/sounds/sniper_reload.wav')
    combatroll = pygame.mixer.Sound('assets/sounds/combatroll.wav')
    lootBody = pygame.mixer.Sound('assets/sounds/loot.wav')
    sawedoffshot = pygame.mixer.Sound('assets/sounds/sawedoffshot.wav')
    sawedoffopen = pygame.mixer.Sound('assets/sounds/sawedoffopen.wav')
    loadshell = pygame.mixer.Sound('assets/sounds/loadshell.wav')
    burp = pygame.mixer.Sound('assets/sounds/burp.wav')
    burp2 = pygame.mixer.Sound('assets/sounds/burp2.wav')
    burp3 = pygame.mixer.Sound('assets/sounds/burp3.wav')
    venom_heartbeat = pygame.mixer.Sound('assets/sounds/venom_heartbeat.wav')
    rattlesnake_rattle = pygame.mixer.Sound('assets/sounds/rattlesnake_rattle.wav')
    rattlesnake_strike = pygame.mixer.Sound('assets/sounds/rattlesnake_strike.wav')
    saloon_ambience = pygame.mixer.Sound('assets/sounds/saloon.wav')
    outside_ambience = pygame.mixer.Sound('assets/sounds/wind.wav')
    train_distant = pygame.mixer.Sound('assets/sounds/train_distant.wav')


# sprites
if collapse:
    asset_cactus = pygame.image.load("assets/vegetation/cactus.png")
    asset_cloud1 = pygame.image.load("assets/sky/cloud1.png")
    asset_cloud2 = pygame.image.load("assets/sky/cloud2.png")
    asset_saloon = pygame.image.load("assets/buildings/cianfarano_saloon_open.png")
    asset_store = pygame.image.load("assets/buildings/solee_os_store.png")
    asset_hotbar = pygame.image.load("assets/UI/hotbar.png")
    asset_revolver_icon = pygame.image.load("assets/UI/revolver_icon.png")
    asset_sniper_icon = pygame.image.load("assets/UI/sniper_rifle_icon.png")
    asset_sawed_off_icon = pygame.image.load("assets/UI/sawed_off_icon.png")
    asset_bandit1left = pygame.image.load("assets/npc/bandit1.png")
    asset_bandit2left = pygame.image.load("assets/npc/bandit2.png")
    asset_bandit3left = pygame.image.load("assets/npc/bandit3.png")
    asset_bandit1right = pygame.image.load("assets/npc/bandit1right.png")
    asset_bandit2right = pygame.image.load("assets/npc/bandit2right.png")
    asset_bandit3right = pygame.image.load("assets/npc/bandit3right.png")
    asset_bandit1left_dead = pygame.image.load("assets/npc/bandit1dead.png")
    asset_bandit2left_dead = pygame.image.load("assets/npc/bandit2dead.png")
    asset_bandit3left_dead = pygame.image.load("assets/npc/bandit3dead.png")
    asset_bandit1right_dead = pygame.image.load("assets/npc/bandit1rightdead.png")
    asset_bandit2right_dead = pygame.image.load("assets/npc/bandit2rightdead.png")
    asset_bandit3right_dead = pygame.image.load("assets/npc/bandit3rightdead.png")
    asset_holster_right = pygame.image.load("assets/player/holster_right.png")
    asset_bandana_right = pygame.image.load("assets/player/bandana_right.png")
    asset_bandana_left = pygame.image.load("assets/player/bandana_left.png")
    asset_revolver_vert_right = pygame.image.load("assets/weapons/revolver_vert_right.png")
    asset_revolver_vert_grip_left = pygame.image.load("assets/weapons/revolver_vert_grip_left.png")
    asset_revolver_right = pygame.image.load("assets/weapons/revolver_right.png")
    asset_revolver_left = pygame.image.load("assets/weapons/revolver_left.png")
    asset_sniper_left = pygame.image.load("assets/weapons/rolling_block_left.png")
    asset_sniper_right = pygame.image.load("assets/weapons/rolling_block_right.png")
    asset_sawed_off_left = pygame.image.load("assets/weapons/sawed_off_left.png")
    asset_sawed_off_right = pygame.image.load("assets/weapons/sawed_off_right.png")
    asset_sawed_off_half_left = pygame.image.load("assets/weapons/sawed_off_left_half.png")
    asset_sawed_off_half_right = pygame.image.load("assets/weapons/sawed_off_right_half.png")
    asset_muzzleflash_right = pygame.image.load("assets/weapons/muzzle_flash_bullet_right.png")
    asset_muzzleflash_left = pygame.image.load("assets/weapons/muzzle_flash_bullet_left.png")
    asset_muzzleflash_buck_right = pygame.image.load("assets/weapons/muzzle_flash_buck_right.png")
    asset_muzzleflash_buck_left = pygame.image.load("assets/weapons/muzzle_flash_buck_left.png")
    asset_sniperscope = pygame.image.load("assets/weapons/sniper_scope.png")
    asset_bandit1_fp = pygame.image.load("assets/npc/bandit1_fp.png")
    asset_bandit2_fp = pygame.image.load("assets/npc/bandit2_fp.png")
    asset_bandit3_fp = pygame.image.load("assets/npc/bandit3_fp.png")
    asset_scope_back_right = pygame.image.load("assets/weapons/scope_back_right.png")
    asset_scope_back_left = pygame.image.load("assets/weapons/scope_back_left.png")
    asset_sniper_rifle_right = pygame.image.load("assets/weapons/sniper_rifle_right.png")
    asset_sniper_rifle_left = pygame.image.load("assets/weapons/sniper_rifle_left.png")
    asset_shop_interior = pygame.image.load("assets/buildings/shop_interior.png")
    asset_saloon_interior = pygame.image.load("assets/buildings/saloon_interior.png")
    asset_text_1000_green = pygame.image.load("assets/UI/text_1000_green.png")
    asset_text_1000_red = pygame.image.load("assets/UI/text_1000_red.png")
    asset_text_3000_green = pygame.image.load("assets/UI/text_3000_green.png")
    asset_text_3000_red = pygame.image.load("assets/UI/text_3000_red.png")
    asset_text_100_green = pygame.image.load("assets/UI/text_100_green.png")
    asset_text_100_red = pygame.image.load("assets/UI/text_100_red.png")
    asset_text_50_green = pygame.image.load("assets/UI/text_50_green.png")
    asset_text_50_red = pygame.image.load("assets/UI/text_50_red.png")
    asset_text_owned = pygame.image.load("assets/UI/text_owned.png")
    asset_text_purchased = pygame.image.load("assets/UI/text_purchased.png")
    asset_text_insufficient = pygame.image.load("assets/UI/text_insufficient.png")
    asset_catalog_1 = pygame.image.load("assets/UI/catalog_pages_1.png")
    asset_catalog_2 = pygame.image.load("assets/UI/catalog_pages_2.png")
    asset_catalog_3 = pygame.image.load("assets/UI/catalog_pages_3.png")
    asset_hp_icon = pygame.image.load("assets/UI/player_hp.png")
    asset_hp_poison_icon = pygame.image.load("assets/UI/player_hp_poison.png")
    asset_money_icon = pygame.image.load("assets/UI/player_money.png")
    asset_kills_icon = pygame.image.load("assets/UI/player_kills.png")
    asset_ammo_icon = pygame.image.load("assets/UI/player_bullet.png")
    asset_journey_cover = pygame.image.load("assets/UI/Journeys_Wild_West_Cover.png")
    asset_player_right = pygame.image.load("assets/player/player_idle_right.png")
    asset_player_left = pygame.image.load("assets/player/player_idle_left.png")
    asset_player_arms_idle = pygame.image.load("assets/player/player_arms_idle.png")
    asset_player_legs_idle_right = pygame.image.load("assets/player/player_legs_idle_right.png")
    asset_player_legs_idle_left = pygame.image.load("assets/player/player_legs_idle_left.png")
    asset_player_arms_walk_right = pygame.image.load("assets/player/player_arms_walk_right.png")
    asset_player_arms_walk_left = pygame.image.load("assets/player/player_arms_walk_left.png")
    asset_player_legs_walk_right = pygame.image.load("assets/player/player_legs_walk_right.png")
    asset_player_legs_walk_left = pygame.image.load("assets/player/player_legs_walk_left.png")
    asset_player_holster_right = pygame.image.load("assets/player/player_arms_holster_right.png")
    asset_player_holster_left = pygame.image.load("assets/player/player_arms_holster_left.png")
    asset_player_holsterwalk_right = pygame.image.load("assets/player/player_arms_holsterwalk_right.png")
    asset_player_holsterwalk_left = pygame.image.load("assets/player/player_arms_holsterwalk_left.png")
    asset_player_shoot_right = pygame.image.load("assets/player/player_shoot_revolver_right.png")
    asset_player_shoot_left = pygame.image.load("assets/player/player_shoot_revolver_left.png")
    asset_player_drink_right = pygame.image.load("assets/player/player_drink_right.png")
    asset_player_drink_left = pygame.image.load("assets/player/player_drink_left.png")
    asset_player_roll1_right = pygame.image.load("assets/player/player_roll1_right.png")
    asset_player_roll2_right = pygame.image.load("assets/player/player_roll2_right.png")
    asset_player_roll3_right = pygame.image.load("assets/player/player_roll3_right.png")
    asset_player_roll1_left = pygame.image.load("assets/player/player_roll1_left.png")
    asset_player_roll2_left = pygame.image.load("assets/player/player_roll2_left.png")
    asset_player_roll3_left = pygame.image.load("assets/player/player_roll3_left.png")
    asset_player_loot_left = pygame.image.load("assets/player/player_loot_left.png")
    asset_player_loot_right = pygame.image.load("assets/player/player_loot_right.png")
    asset_player_cooldown_sweat_right = pygame.image.load("assets/player/cooldown_sweat_right.png")
    asset_player_cooldown_sweat_left = pygame.image.load("assets/player/cooldown_sweat_left.png")
    asset_player_hp_gain_particle = pygame.image.load("assets/player/hp_gain_particle.png")
    asset_hearty_beer_icon = pygame.image.load("assets/UI/hearty_beer_icon.png")
    asset_hearty_beer_right = pygame.image.load("assets/props/hearty_beer_right.png")
    asset_hearty_beer_left = pygame.image.load("assets/props/hearty_beer_left.png")
    asset_death_screen = pygame.image.load("assets/UI/death_screen.png")
    asset_sky_day = pygame.image.load("assets/sky/sky_day.png")
    asset_tumbleweed = pygame.image.load("assets/vegetation/tumbleweed.png")
    asset_ground_sand = pygame.image.load("assets/vegetation/ground_sand.png")
    asset_hotbar_select = pygame.image.load("assets/UI/hotbar_select.png")
    asset_main_menu = pygame.image.load("assets/UI/main_menu2.png")
    asset_button_normal = pygame.image.load("assets/UI/button_normal.png")
    asset_button_hover = pygame.image.load("assets/UI/button_hover.png")
    asset_button_clicked = pygame.image.load("assets/UI/button_clicked.png")
    asset_restart_button_normal = pygame.image.load("assets/UI/restart_button_normal.png")
    asset_restart_button_hover = pygame.image.load("assets/UI/restart_button_hover.png")
    asset_restart_button_clicked = pygame.image.load("assets/UI/restart_button_clicked.png")
    asset_main_menu_button_normal = pygame.image.load("assets/UI/main_menu_button_normal.png")
    asset_main_menu_button_hover = pygame.image.load("assets/UI/main_menu_button_hover.png")
    asset_main_menu_button_clicked = pygame.image.load("assets/UI/main_menu_button_clicked.png")
    asset_paused_overlay = pygame.image.load("assets/UI/paused.png")
    asset_paused_darken = pygame.image.load("assets/UI/pause_darken.png")
    asset_resume_button_normal = pygame.image.load("assets/UI/resume_button_normal.png")
    asset_resume_button_hover = pygame.image.load("assets/UI/resume_button_hover.png")
    asset_resume_button_clicked = pygame.image.load("assets/UI/resume_button_clicked.png")
    asset_settings_button_normal = pygame.image.load("assets/UI/settings_button_normal.png")
    asset_settings_button_hover = pygame.image.load("assets/UI/settings_button_hover.png")
    asset_settings_button_clicked = pygame.image.load("assets/UI/settings_button_clicked.png")
    asset_main_menu2_button_normal = pygame.image.load("assets/UI/main_menu2_button_normal.png")
    asset_main_menu2_button_hover = pygame.image.load("assets/UI/main_menu2_button_hover.png")
    asset_main_menu2_button_clicked = pygame.image.load("assets/UI/main_menu2_button_clicked.png")
    asset_confirm_yes_button_normal = pygame.image.load("assets/UI/confirm_yes_button_normal.png")
    asset_confirm_yes_button_hover = pygame.image.load("assets/UI/confirm_yes_button_hover.png")
    asset_confirm_yes_button_clicked = pygame.image.load("assets/UI/confirm_yes_button_clicked.png")
    asset_confirm_no_button_normal = pygame.image.load("assets/UI/confirm_no_button_normal.png")
    asset_confirm_no_button_hover = pygame.image.load("assets/UI/confirm_no_button_hover.png")
    asset_confirm_no_button_clicked = pygame.image.load("assets/UI/confirm_no_button_clicked.png")
    asset_confirmation_box = pygame.image.load("assets/UI/confirmation.png")
    asset_settings_menu = pygame.image.load("assets/UI/settings.png")
    asset_settings_done_button_normal = pygame.image.load("assets/UI/settings_done_button_normal.png")
    asset_settings_done_button_hover = pygame.image.load("assets/UI/settings_done_button_hover.png")
    asset_settings_done_button_clicked = pygame.image.load("assets/UI/settings_done_button_clicked.png")
    asset_master_left_button_normal = pygame.image.load("assets/UI/master_left_button_normal.png")
    asset_master_left_button_hover = pygame.image.load("assets/UI/master_left_button_hover.png")
    asset_master_left_button_clicked = pygame.image.load("assets/UI/master_left_button_clicked.png")
    asset_master_right_button_normal = pygame.image.load("assets/UI/master_right_button_normal.png")
    asset_master_right_button_hover = pygame.image.load("assets/UI/master_right_button_hover.png")
    asset_master_right_button_clicked = pygame.image.load("assets/UI/master_right_button_clicked.png")
    asset_music_left_button_normal = pygame.image.load("assets/UI/music_left_button_normal.png")
    asset_music_left_button_hover = pygame.image.load("assets/UI/music_left_button_hover.png")
    asset_music_left_button_clicked = pygame.image.load("assets/UI/music_left_button_clicked.png")
    asset_music_right_button_normal = pygame.image.load("assets/UI/music_right_button_normal.png")
    asset_music_right_button_hover = pygame.image.load("assets/UI/music_right_button_hover.png")
    asset_music_right_button_clicked = pygame.image.load("assets/UI/music_right_button_clicked.png")
    asset_music_icon_button_normal = pygame.image.load("assets/UI/music_icon_button_normal.png")
    asset_music_icon_button_hover = pygame.image.load("assets/UI/music_icon_button_hover.png")
    asset_music_icon_button_clicked = pygame.image.load("assets/UI/music_icon_button_clicked.png")
    asset_master_icon_button_normal = pygame.image.load("assets/UI/master_icon_button_normal.png")
    asset_master_icon_button_hover = pygame.image.load("assets/UI/master_icon_button_hover.png")
    asset_master_icon_button_clicked = pygame.image.load("assets/UI/master_icon_button_clicked.png")
    asset_volume_muted_strikethrough = pygame.image.load("assets/UI/muted_crossout.png")
    asset_exit_button = pygame.image.load("assets/UI/exit_button.png")
    asset_exit_button_hover = pygame.image.load("assets/UI/exit_button_hover.png")
    asset_rattlesnake1_left = pygame.image.load("assets/npc/rattlesnake1_left.png")
    asset_rattlesnake2_left = pygame.image.load("assets/npc/rattlesnake2_left.png")
    asset_rattlesnake_strike_left = pygame.image.load("assets/npc/rattlesnake_strike_left.png")
    asset_rattlesnake_dead_left = pygame.image.load("assets/npc/rattlesnake_dead_left.png")
    asset_rattlesnake1_right = pygame.image.load("assets/npc/rattlesnake1_right.png")
    asset_rattlesnake2_right = pygame.image.load("assets/npc/rattlesnake2_right.png")
    asset_rattlesnake_strike_right = pygame.image.load("assets/npc/rattlesnake_strike_right.png")
    asset_rattlesnake_dead_right = pygame.image.load("assets/npc/rattlesnake_dead_right.png")
    asset_buy_hover_p1_1 = pygame.image.load("assets/UI/buy_hover_p1_1.png")
    asset_buy_hover_p1_2 = pygame.image.load("assets/UI/buy_hover_p1_2.png")
    asset_buy_hover_p1_3 = pygame.image.load("assets/UI/buy_hover_p1_3.png")
    asset_buy_hover_p2_1 = pygame.image.load("assets/UI/buy_hover_p2_1.png")
    asset_buy_hover_p2_2 = pygame.image.load("assets/UI/buy_hover_p2_2.png")
    asset_buy_hover_p2_3 = pygame.image.load("assets/UI/buy_hover_p2_3.png")
    asset_buy_hover_p2_4 = pygame.image.load("assets/UI/buy_hover_p2_4.png")

# text
if collapse:
    font1 = pygame.font.Font("assets/fonts/BAHNSCHRIFT.TTF", 13)
    font2 = pygame.font.Font("assets/fonts/BAHNSCHRIFT.TTF", 18)
    font3 = pygame.font.SysFont("ebrima", 20, True)
    font4 = pygame.font.Font("assets/fonts/BAHNSCHRIFT.TTF", 16)
    font5 = pygame.font.Font("assets/fonts/BAHNSCHRIFT.TTF", 24)
    # syntax - (Name, Size, Bold, Italic)

    playerHP_text = font2.render((str(playerHP)), True, (255,255,255))
    playerScore_text = font2.render((str(score)), True, (255,255,255))
    playerMoney_text = font2.render((str(moneyCount)), True, (255,255,255))
    revolverAmmo_text = font2.render((str(revRoundsMag) + "/" + str(revRoundsTotal)), True, (255,255,255))
    sniperAmmo_text = font2.render((str(sniperRoundsMag) + "/" + str(sniperRoundsTotal)), True, (255,255,255))
    sawedOffAmmo_text = font2.render((str(sawedOffRoundsMag) + "/" + str(buckRoundsTotal)), True, (255, 255, 255))
    blankAmmo_text = font2.render("-", True, (255,255,255))
    if demoMode == True:
        reload_text = font1.render("RELOAD (R)", True, (255, 0, 0))
    else:
        reload_text = font1.render("RELOAD", True, (255, 0, 0))
    outAmmo_text = font1.render("Out of Ammo", True, (255,0,0))
    if demoMode == True:
        interact_text = font1.render("ACTION (W)", True, (150, 240, 41))
    else:
        interact_text = font1.render("INTERACT", True, (255,255,255))
    buy_text = font1.render("BUY", True, (255,255,255))
    potionCount_text = font1.render((str(hpPotionCount)), True, (255,255,255))
    clickPlay_text = font1.render("Click Here to PLAY", True, (255,255,255))
    deathScore_text = font2.render(("Score: " + str(score)), True, (255,255,255))
    shopWarning_text = font1.render("\"Take your hand off the gun, son..\"", True, (0, 0, 0))
    version_text = font1.render(("v " + version), True, (255, 255, 255))
    masterVolume_text = font1.render((str(masterVolume)), True, (255, 255, 255))
    musicVolume_text = font1.render((str(musicVolume)), True, (255, 255, 255))
    playerHighscore_text = font1.render("Highscore: " + (str(highscore)), True, (255, 255, 255))
    if demoMode == True:
        loot_text = font1.render("LOOT (F)", True, (255, 255, 255))
    else:
        loot_text = font1.render("LOOT", True, (255, 255, 255))

    moneyGained_text = font4.render("+ $", True, (50, 100, 50))
    wave_text = font5.render("Wave " + str(wave), True, (240, 177, 29))
    wave_text_rect = wave_text.get_rect(center=[300, 150])
    infinity_text = font2.render("-1", True, (255,255,255))
    if demoMode == True:
        devMode_text = font1.render("Demo Mode", True, (255, 255, 255))
    else:
        devMode_text = font1.render("Dev Mode", True, (255, 255, 255))
    # syntax - (Message, AntiAliasing, Color, Background=None)

# list of names
list_names = ['Bob', 'Richard', 'Aaron', 'Arthur', 'Henry', 'Frank', 'Edward', 'Albert','James', 'John', 'Walter',
              'Roy', 'Louis', 'Carl', 'Paul', 'Pedro', 'Samuel', 'Ray', 'Howard', 'Oscar', 'Leo', 'Jack', 'Lee']


# enemy methods
def getEnemyRespawn():
    x = random.randint(-2500, 2500)
    if x <= 1000 and x >= 300:
        x += 900
    if x >= -400 and x < 300:
        x -= 900
    return x


# Bandit class
class Bandit:
    # instance list for created bandits
    instances = []
    alive = 0

    # dictionary for types of bandits
    TYPE_MAP = {
                1: (asset_bandit1left, asset_bandit1right, asset_bandit1left_dead, asset_bandit1right_dead, asset_bandit1_fp),
                2: (asset_bandit2left, asset_bandit2right, asset_bandit2left_dead, asset_bandit2right_dead, asset_bandit2_fp),
                3: (asset_bandit3left, asset_bandit3right, asset_bandit3left_dead, asset_bandit3right_dead, asset_bandit3_fp)
                }

    # constructor
    def __init__(self):
        Bandit.alive += 1
        self.__class__.instances.append(self)
        self.name = random.choice(list_names)  # assign random name
        self.bandit_left_img, self.bandit_right_img, self.bandit_leftdead_img, self.bandit_rightdead_img, self.bandit_fp_img = \
            self.TYPE_MAP[random.randint(1,3)]  # assign random type
        self.level = 1  # assign level
        self.hp = 100  # assign starting hp
        self.x_location = getEnemyRespawn()  # assign x-location
        self.moveSpeed = 8
        self.bandit_left = None  # is the bandit on the left side of player
        self.nameTag = font1.render("Bandit: " + self.name, True, (150, 240, 41))
        self.hpTag = font1.render(("HP: " + str(self.hp)), True, (255,255,255))
        self.nameLength = len(self.name)
        self.banW = 200  # bandit fp img width
        self.banH = 330  # bandit fp img height
        self.stoodOn = False  # is the bandit being stood on by player
        self.looted = False  # has the player looted bandit

    # general method that calls all of the other methods, will be called constantly by main
    def work(self):
        self.move(self.moveSpeed)
        self.draw()
        self.checkMelee()
        self.checkDead()

    # bandit movement
    def move(self, vel):
        # bandit is right of player
        if self.hp > 0 and banMoveAbility == True and invisible == False:
            if self.x_location >= 280:
                self.x_location -= vel
                self.bandit_left = False
            # bandit is left of player
            elif self.x_location <= 220:
                self.x_location += vel
                self.bandit_left = True

    # draws alive bandit
    def draw(self):
        # refresh hp tag
        self.hpTag = font1.render(("HP: " + str(self.hp)), True, (255, 255, 255))
        # draw alive bandit
        if self.hp > 0:
            if displayHUD == True:
                screen.blit(self.nameTag, (self.x_location-20-self.nameLength,232))
                screen.blit(self.hpTag, (self.x_location-7,246))
            if self.bandit_left == False:
                screen.blit(self.bandit_left_img, (self.x_location-39.5, 262))
            elif self.bandit_left == True:
                screen.blit(self.bandit_right_img, (self.x_location-7, 262))

    # seperate from draw method so that it can be called after drawing the player
    def draw_dead(self):
        # draw dead bandit
        if insideShop == False and insideSaloon == False:
            if self.hp <= 0:
                if self.bandit_left == False:
                    screen.blit(self.bandit_leftdead_img, (self.x_location-23, 377))
                elif self.bandit_left == True:
                    screen.blit(self.bandit_rightdead_img, (self.x_location-123, 377))

    # cheks if bandit is in melee range
    def checkMelee(self):
        if self.hp > 0:
            if self.x_location <= 290 and self.x_location >= 210 and insideShop == False and insideSaloon == False:
                playerHit(4)

    # checks if bandit is dead, looted, and when it should despawn
    def checkDead(self):
        # bandit dead
        if self.hp == 0:
            banpain.play()
            giveScore()
            Bandit.alive -= 1
            self.hp -= 1
        # if player is on top of body
        if self.x_location <= 260 and self.x_location >= 120 and self.bandit_left == False \
                or self.x_location <= 360 and self.x_location >= 220 and self.bandit_left == True and self.hp <= 0:
            self.stoodOn = True
        else:
            self.stoodOn = False
        # decrease hp if dead and looted
        if self.hp <= 0 and self.looted == True:
            self.hp -= 1
        # remove from instance list
        if self.hp <= -20:
            # self.respawn()
            self.instances.remove(self)

    # manual respawn if needed
    def respawn(self):
        self.hp = 100
        self.x_location = getEnemyRespawn()
        self.looted = False


# Rattlesnake class
class Rattlesnake:
    # instance list for created rattlesnakes
    instances = []
    alive = 0

    # dictionary for types of rattlesnakes
    TYPE_MAP = {
                1: (asset_rattlesnake1_left, asset_rattlesnake2_left, asset_rattlesnake_strike_left, asset_rattlesnake_dead_left,
                    asset_rattlesnake1_right, asset_rattlesnake2_right, asset_rattlesnake_strike_right, asset_rattlesnake_dead_right)
                }

    # constructor
    def __init__(self, x = 0):
        Rattlesnake.alive += 1
        self.__class__.instances.append(self)
        self.snake1_left_img, self.snake2_left_img, self.snake_strike_left_img, self.snake_dead_left_img, \
            self.snake1_right_img, self.snake2_right_img, self.snake_strike_right_img, self.snake_dead_right_img = \
            self.TYPE_MAP[random.randint(1,1)]  # assign random type
        self.level = 1  # assign level
        self.hp = 15  # assign starting hp
        if x == 0:
            self.x_location = getEnemyRespawn()  # assign x-location
        else:
            self.x_location = x  # assign x-location
        self.rattlesnake_left = None  # is the bandit on the left side of player
        self.nameTag = font1.render("Rattlesnake", True, (150, 240, 41))
        self.hpTag = font1.render(("HP: " + str(self.hp)), True, (255,255,255))
        self.stoodOn = False  # is the bandit being stood on by player
        self.looted = False  # has the player looted bandit
        self.rattle_range = 350  # distance player needs to be from snake for it to rattle
        self.strike_range = 100  # distance player needs to be from snake for it to rattle
        self.rattleInRange = False  # is the player close enough to the rattlesnake to where it will rattle
        self.rattle_state = 0  # state of rattle the snake is in
        self.strikeCooldown = False  # is the snake's attack in cooldown
        self.rattleCooldown = False  # is the snake's rattle in cooldown
        self.rattleSoundCooldown = False  # is the snake's rattle in cooldown
        self.striking = False  # is the snake striking/attacking player

    # general method that calls all of the other methods, will be called constantly by main
    def work(self):
        self.draw()
        self.move()
        self.checkMelee()
        self.checkDead()

    # rattlesnake movement
    def move(self):
        # rattlesnake is right of player
        if self.hp > 0:
            if self.x_location >= 240:
                self.rattlesnake_left = False
            # bandit is left of player
            elif self.x_location <= 270:
                self.rattlesnake_left = True

    # rattlesnake movement
    def strike(self):
        # rattlesnake is right of player
        if self.hp > 0 and self.strikeCooldown == False:
            snakeStrikeStop_timer.stop()
            self.striking = True
            self.strikeCooldown = True
            rattlesnake_strike.play()
            snakeStrikeStop_timer.start()
            snakeStrikeCooldown_timer.start()
            if invincibility == False:
                playerHit(10)
                venomed(10)

    # snake rattles
    def rattle(self):
        self.rattleCooldown = True
        if self.rattleSoundCooldown == False:
            rattlesnake_rattle.play()
        self.rattleSoundCooldown = True
        # play audio
        # change states
        if self.rattle_state == 0:
            self.rattle_state = 1
        elif self.rattle_state == 1:
            self.rattle_state = 0
        # start cooldown timer
        snakeRattleCooldown_timer.start()
        snakeRattleSoundCooldown_timer.start()

    # draws alive rattlesnake
    def draw(self):
        # refresh hp tag
        self.hpTag = font1.render(("HP: " + str(self.hp)), True, (255, 255, 255))
        # draw alive rattlesnake
        if self.hp > 0:
            if displayHUD == True:
                screen.blit(self.nameTag, (self.x_location+1,322))
                screen.blit(self.hpTag, (self.x_location+15,336))
            if self.rattlesnake_left == False:
                if self.striking == False:
                    if self.rattle_state == 0:
                        screen.blit(self.snake1_left_img, (self.x_location-39.5, 347))
                    if self.rattle_state == 1:
                        screen.blit(self.snake2_left_img, (self.x_location-39.5, 347))
                if self.striking == True:
                    screen.blit(self.snake_strike_left_img, (self.x_location - 39.5, 347))
            elif self.rattlesnake_left == True:
                if self.striking == False:
                    if self.rattle_state == 0:
                        screen.blit(self.snake1_right_img, (self.x_location-7, 347))
                    if self.rattle_state == 1:
                        screen.blit(self.snake2_right_img, (self.x_location-7, 347))
                if self.striking == True:
                    screen.blit(self.snake_strike_right_img, (self.x_location - 7, 347))

    # seperate from draw method so that it can be called after drawing the player
    def draw_dead(self):
        # draw dead rattlesnake
        if insideShop == False and insideSaloon == False:
            if self.hp <= 0:
                if self.rattlesnake_left == False:
                    screen.blit(self.snake_dead_left_img, (self.x_location-39.5, 347))
                elif self.rattlesnake_left == True:
                    screen.blit(self.snake_dead_right_img, (self.x_location-7, 347))

    # cheks if rattlesnake is in melee range
    def checkMelee(self):
        if self.hp > 0:
            if self.x_location <= 210+self.rattle_range and self.x_location >= 210-self.rattle_range and insideShop == False \
                    and insideSaloon == False:
                if self.rattleCooldown == False:
                    self.rattle()
            if self.x_location <= 210+self.strike_range and self.x_location >= 210-self.strike_range and insideShop == False \
                    and insideSaloon == False:
                if self.strikeCooldown == False:
                    self.strike()

    # checks if rattlesnake is dead, looted, and when it should despawn
    def checkDead(self):
        # bandit dead
        if self.hp == 0:
            rattlesnake_rattle.stop()
            giveScore()
            Rattlesnake.alive -= 1
            self.hp -= 1
        # if player is on top of body
        if self.x_location <= 260 and self.x_location >= 120 and self.rattlesnake_left == False \
                or self.x_location <= 360 and self.x_location >= 220 and self.rattlesnake_left == True and self.hp <= 0:
            self.stoodOn = True
        else:
            self.stoodOn = False
        # decrease hp if dead and looted
        if self.hp <= 0 and self.looted == True:
            self.hp -= 1
        # remove from instance list
        if self.hp <= -20:
            # self.respawn()
            self.instances.remove(self)

    # manual respawn if needed
    def respawn(self):
        self.hp = 100
        self.x_location = getEnemyRespawn()
        self.looted = False




def worldLeft(multiplier=1):
    global cloud1x, cloud2x, standing, cactusx, store1x, store2x, tumweed1x,\
        playerIdle, playerWalk, playerLegsIdle, playerShoot, playerHolster, playerSniper

    if standing == True:
        playerIdle = False
        playerLegsIdle = False
        if playerShoot == True:
            playerHolster = True
            playerShoot = False
        if lookingRight == True:
            playerWalk = True
        if lookingLeft == True:
            playerWalk = True

    cloud1x += cloudMove*multiplier
    if cloud1x + 85 >= 800:
        cloud1x = -100
    cloud2x += cloudMove*multiplier
    if cloud2x + 85 >= 800:
        cloud2x = -100
    cactusx += speedMove*multiplier
    store1x += speedMove*multiplier
    store2x += speedMove*multiplier
    tumweed1x += speedMove*multiplier

    # move bandits
    for instance in Bandit.instances:
        instance.x_location += speedMove*multiplier

    # move rattlesnakes
    for instance in Rattlesnake.instances:
        instance.x_location += speedMove*multiplier


def worldRight(multiplier=1):
    global cloud1x, cloud2x, standing, cactusx, store1x, store2x, tumweed1x, \
        playerIdle, playerWalk, playerLegsIdle, playerShoot, playerHolster, playerSniper

    if standing == True:
        playerIdle = False
        playerLegsIdle = False
        if playerShoot == True:
            playerHolster = True
            playerShoot = False
        if lookingRight == True:
            playerWalk = True
        if lookingLeft == True:
            playerWalk = True
        if playerShoot == True:
            playerHolster = True

    cloud1x -= cloudMove*multiplier
    if cloud1x + 85 <= -100:
        cloud1x = 800
    cloud2x -= cloudMove*multiplier
    if cloud2x + 85 <= -100:
        cloud2x = 1100
    cactusx -= speedMove*multiplier
    store1x -= speedMove*multiplier
    store2x -= speedMove*multiplier
    tumweed1x -= speedMove*multiplier

    # move bandits
    for instance in Bandit.instances:
        instance.x_location -= speedMove*multiplier

    # move rattlesnake
    for instance in Rattlesnake.instances:
        instance.x_location -= speedMove*multiplier


def walkRight():
    global moveAbility, hotbarSlot2, moneyPickText, interactText, insufFundsText, purchasedText, lookingRight,\
        lookingLeft, hotbarSlot1, store1x, store2x, scopeScreen, insideShop, playerShoot, playerHolster,\
        banMoveAbility, cactusx, insideSaloon
    if moveAbility == True and pause == False and rolling == False:
        if scopeScreen == False:
            worldRight()
            disableText()
            lookingRight = True
            lookingLeft = False
            if hotbarSlot1 == True:
                playerHolster = True
            if hotbarSlot3 == True and ownSawedOff:
                playerHolster = True
            if insideShop == False and insideSaloon == False:
                step.stop()
                step.play()
            elif insideShop == True or insideSaloon == True:
                woodstep.stop()
                woodstep.play()

    # Shop Wall Collision
    if insideShop == True:
        if (store1x + 700) <= 0:
            moveAbility = False

    # Saloon Wall Collision
    if insideSaloon == True:
        if (store2x + 700) <= 0:
            moveAbility = False


def walkLeft():
    global moveAbility, hotbarSlot2, moneyPickText, interactText, insufFundsText, purchasedText, lookingRight,\
        lookingLeft, hotbarSlot1, store1x, store2x, scopeScreen, insideShop, playerShoot, playerHolster,\
        banMoveAbility, cactusx, insideSaloon

    if moveAbility == True and pause == False and rolling == False:
        if scopeScreen == False:
            worldLeft()
            disableText()
            lookingRight = False
            lookingLeft = True
            if hotbarSlot1 == True:
                playerHolster = True
            if hotbarSlot3 == True and ownSawedOff:
                playerHolster = True
            if insideShop == False and insideSaloon == False:
                step.stop()
                step.play()
            elif insideShop == True or insideSaloon == True:
                woodstep.stop()
                woodstep.play()
    # Exit Store
    if insideShop == True and insideSaloon == False:
        if (store1x - 200) >= 0:
            insideShop = False
            store1x = 50
            store2x = 750
            cactusx = -200
            banMoveAbility = True
            door.stop()
            door.play()
            outside_ambience.play(-1)
    # Shop Wall Collision
    if insideShop == True:
        if (store1x + 700) <= 0:
            moveAbility = True
            walkLeft()

    # Exit Saloon
    if insideSaloon == True and insideShop == False:
        if (store2x - 200) >= 0:
            insideSaloon = False
            store1x = -650
            store2x = 50
            cactusx = -900
            banMoveAbility = True
            door.stop()
            door.play()
            saloon_ambience.stop()
            outside_ambience.play(-1)
    # Shop Wall Collision
    if insideSaloon == True:
        if (store2x + 700) <= 0:
            moveAbility = True
            walkLeft()


def checkWalkBoth():
    global walkingBoth
    # If trying to walk both left and right
    if walkingLeft and walkingRight:
        walkingBoth = True
    else:
        walkingBoth = False


def roll():
    global moveAbility, hotbarSlot2, moneyPickText, interactText, insufFundsText, purchasedText, lookingRight,\
        lookingLeft, hotbarSlot1, store1x, store2x, scopeScreen, insideShop, playerShoot, playerHolster, playerSniper,\
        insideSaloon
    if lookingRight:
        if moveAbility == True and pause == False:
            if rollReady == True:
                disableText()
                # start roll
                rollStart_timer.start()
                lookingRight = True
                lookingLeft = False
                if hotbarSlot1 == True:
                    playerHolster = True
                if hotbarSlot3 == True and ownSawedOff:
                    playerHolster = True
                if insideShop == False and insideSaloon == False:
                    step.stop()
                    step.play()
                elif insideShop == True or insideSaloon == True:
                    woodstep.stop()
                    woodstep.play()
    elif lookingLeft:
        if moveAbility == True and pause == False:
            if rollReady == True:
                disableText()
                # start roll
                rollStart_timer.start()
                lookingRight = False
                lookingLeft = True
                if hotbarSlot1 == True:
                    playerHolster = True
                if hotbarSlot3 == True and ownSawedOff:
                    playerHolster = True
                if insideShop == False and insideSaloon == False:
                    step.stop()
                    step.play()
                elif insideShop == True or insideSaloon == True:
                    woodstep.stop()
                    woodstep.play()


def loot():
    global playerHolster, looting, standing, moveAbility

    if moveAbility == True and pause == False:
        disableText()
        if hotbarSlot1 == True:
            playerHolster = True
        if hotbarSlot3 == True and ownSawedOff:
            playerHolster = True
        looting = True
        standing = False
        moveAbility = False
        giveMoney()
        lootBody.play()
        loot_timer.start()


def disableText():
    global moneyPickText, interactText, insufFundsText, purchasedText
    moneyPickText = False
    insufFundsText = False
    purchasedText = False


def scoped():
    global scopeWalk
    # backdrop
    if lookingRight == True:
        screen.blit(asset_scope_back_right, (0, 0))
    if lookingLeft == True:
        screen.blit(asset_scope_back_left, (0, 0))

    for bandit in Bandit.instances:
        # update bandit scale
        asset_ban_fp = pygame.transform.scale(bandit.bandit_fp_img, (bandit.banW + (scopeWalk * 0.7), bandit.banH + scopeWalk))
        asset_ban_fp_rect = asset_ban_fp.get_rect(center=[300, 330])
        # draw bandit
        if bandit.hp > 0:
            if bandit.x_location <= 700 and bandit.x_location >= 250 and lookingRight == True \
                    or bandit.x_location >= -100 and bandit.x_location <= 250 and lookingLeft == True:
                screen.blit(asset_ban_fp, asset_ban_fp_rect)

    # scope
    screen.blit(asset_sniperscope, (0, 0))
    screen.blit(asset_ammo_icon, (25 - 12.5, 583 - 10))
    screen.blit(sniperAmmo_text, (41, 571))


def fire():
    global score, moneyCount, startGame, moveAbility, hotbarSlot2, hotbarSlot6, dead, bulletx, hotbarSlot1, \
        lookingLeft, lookingRight, revRoundsMag, reloadUI, outAmmoUI, interactText, scopeScreen,\
        playerShoot, playerHolster, revRoundsTotal,sniperRoundsMag, sniperRoundsTotal, playerSniper, pause, \
        sawedOffRoundsMag, insideShop, reloading, insideSaloon

    # Revolver
    if hotbarSlot1 == True:
        playerShoot = True
        playerHolster = False
        shot.stop()
        shot.play()
        revRoundsMag -= 1
        bulletx = 330
        stopReload()
        if insideShop == False and insideSaloon == False:
            if lookingRight:
                # Damage Bandit
                for bandit in Bandit.instances:
                    if bandit.x_location <= 600 and bandit.x_location >= 250:
                        for i in range(0,revolverDamage):
                            if bandit.hp > 0:
                                bandit.hp -= 1
                # Damage Rattlesnake
                for rattlesnake in Rattlesnake.instances:
                    if rattlesnake.x_location <= 600 and rattlesnake.x_location >= 250:
                        for i in range(0,revolverDamage):
                            if rattlesnake.hp > 0:
                                rattlesnake.hp -= 1
            if lookingLeft:
                # Damage Bandit
                for bandit in Bandit.instances:
                    if bandit.x_location >= -50 and bandit.x_location <= 250:
                        for i in range(0,revolverDamage):
                            if bandit.hp > 0:
                                bandit.hp -= 1
                # Damage Rattlesnake
                for rattlesnake in Rattlesnake.instances:
                    if rattlesnake.x_location >= -50 and rattlesnake.x_location <= 250:
                        for i in range(0,revolverDamage):
                            if rattlesnake.hp > 0:
                                rattlesnake.hp -= 1

    # sniper rifle
    if hotbarSlot2 == True and scopeScreen == True:
        interactText = False
        snipershot.stop()
        snipershot.play()
        scopeScreen = False
        sniperRoundsMag -= 1
        stopReload()
        if insideShop == False and insideSaloon == False:
            if lookingRight:
                # Damage Bandit
                for bandit in Bandit.instances:
                    if bandit.x_location <= 700 and bandit.x_location >= 250:
                        for i in range(0,sniperDamage):
                            if bandit.hp > 0:
                                bandit.hp -= 1
                # Damage Rattlesnake
                for rattlesnake in Rattlesnake.instances:
                    if rattlesnake.x_location <= 700 and rattlesnake.x_location >= 250:
                        for i in range(0,sniperDamage):
                            if rattlesnake.hp > 0:
                                rattlesnake.hp -= 1
            if lookingLeft:
                # Damage Bandit
                for bandit in Bandit.instances:
                    if bandit.x_location >= -100 and bandit.x_location <= 250:
                        for i in range(0,sniperDamage):
                            if bandit.hp > 0:
                                bandit.hp -= 1
                # Damage Rattlesnake
                for rattlesnake in Rattlesnake.instances:
                    if rattlesnake.x_location >= -100 and rattlesnake.x_location <= 250:
                        for i in range(0,sniperDamage):
                            if rattlesnake.hp > 0:
                                rattlesnake.hp -= 1

    # sawed off
    if hotbarSlot3 == True:
        playerShoot = True
        playerHolster = False
        interactText = False
        bulletx = 330
        sawedoffshot.stop()
        sawedoffshot.play()
        sawedOffRoundsMag -= 1
        stopReload()
        if insideShop == False and insideSaloon == False:
            if lookingRight:
                # Damage Bandit
                for bandit in Bandit.instances:
                    if bandit.x_location <= 600 and bandit.x_location >= 250:
                        for i in range(0,sawedOffDamage):
                            if bandit.hp > 0:
                                bandit.hp -= 1
                # Damage Rattlesnake
                for rattlesnake in Rattlesnake.instances:
                    if rattlesnake.x_location <= 600 and rattlesnake.x_location >= 250:
                        for i in range(0,sawedOffDamage):
                            if rattlesnake.hp > 0:
                                rattlesnake.hp -= 1
            if lookingLeft:
                # Damage Bandit
                for bandit in Bandit.instances:
                    if bandit.x_location >= -50 and bandit.x_location <= 250:
                        for i in range(0,sawedOffDamage):
                            if bandit.hp > 0:
                                bandit.hp -= 1
                # Damage Rattlesnake
                for rattlesnake in Rattlesnake.instances:
                    if rattlesnake.x_location >= -50 and rattlesnake.x_location <= 250:
                        for i in range(0,sawedOffDamage):
                            if rattlesnake.hp > 0:
                                rattlesnake.hp -= 1


def hpPotion():
    global playerHP, hpPotionCount, playerDrink, playerIdle,beerRegenAmount,healQueue
    beerHealing_timer.start()
    hpPotionCount -= 1
    # adds amount that beer heals to heal queue (will be decremented in beerHealing_timer)
    healQueue += beerRegenAmount
    playerDrink = True
    playerIdle = False
    drinkResetDelay_timer.start()
    potion.play()
    burp.stop()
    burp2.stop()
    burp_timer.start()


def giveMoney(amount = 0):
    global moneyCount, showMoneyGainedText, moneyGained_text
    # if amount wasn't provided
    if amount == 0:
        amount = random.randint(50,100)
    showMoneyGained_timer.stop()
    moneyCount += amount
    moneyGained_text = font4.render("+ $" + (str(amount)), True, (42, 235, 48))
    showMoneyGainedText = True
    showMoneyGained_timer.start()


def giveScore(amount = 1):
    global score
    score += amount


def stopSounds():
    intro.stop()
    reload.stop()
    sniper_reload.stop()
    heartbeat.stop()
    breath.stop()
    intromusic.stop()
    music.stop()
    snipershot.stop()
    shot.stop()
    death.stop()
    playerhit.stop()
    combatroll.stop()


def mainMenu():
    global startGame, tumbleAuto, playButtonHover, moveAbility, banMoveAbility, mouse_posx, mouse_posy, \
        settingsButtonHover, exitButtonHover
    # Background
    screen.blit(asset_main_menu, (0, 0))
    # Version Number
    screen.blit(version_text, (6, 580))
    # Play Button ---------------------------------------------------------------------------------
    # Hover Button
    if (235 <= mouse_posx <= 365) and (420 <= mouse_posy <= 465) and settings == False and playButtonClicked == False:
        screen.blit(asset_button_hover, (0, 0))
        playButtonHover = True
    # Click Button
    elif (235 <= mouse_posx <= 365) and (420 <= mouse_posy <= 465) and playButtonClicked == True:
        screen.blit(asset_button_clicked, (0, 0))
        playButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_button_normal, (0, 0))
        playButtonHover = False
    # Exit Button
    # Hover Button
    if (563 <= mouse_posx <= 592) and (9 <= mouse_posy <= 38) and settings == False:
        screen.blit(asset_exit_button_hover, (0, 0))
        exitButtonHover = True
    # Normal Button
    else:
        screen.blit(asset_exit_button, (0, 0))
        exitButtonHover = False

    # Settings Button -------------------------------------------------------------------------------
    # Hover Button
    if (235 <= mouse_posx <= 367) and (494 <= mouse_posy <= 540) and settingsButtonClicked == False \
            and settings == False:
        screen.blit(asset_settings_button_hover, (0, 170))
        settingsButtonHover = True
    # Click Button
    elif (235 <= mouse_posx <= 367) and (494 <= mouse_posy <= 540) and settingsButtonClicked == True:
        screen.blit(asset_settings_button_clicked, (0, 170))
        settingsButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_settings_button_normal, (0, 170))
        settingsButtonHover = False
    # In Settings Menu
    if settings == True:
        showSettings()
    moveAbility = False
    banMoveAbility = False
    music_timer.stop()


def pauseGame():
    global resumeButtonHover, settingsButtonHover, mainMenu2ButtonHover, confirmYesButtonHover, \
        confirmNoButtonHover, settingsDoneButtonHover, masterLeftButtonHover, masterRightButtonHover, \
        musicLeftButtonHover, musicRightButtonHover

    # Pause Screen -------------------------------------------------------------------------------
    screen.blit(asset_paused_overlay, (0, 0))
    # Resume Button ------------------------------------------------------------------------------
    # Hover Button
    if (235 <= mouse_posx <= 367) and (257 <= mouse_posy <= 302) and resumeButtonClicked == False \
            and confirmationBox == False:
        screen.blit(asset_resume_button_hover, (0, 0))
        resumeButtonHover = True
    # Click Button
    elif (235 <= mouse_posx <= 367) and (257 <= mouse_posy <= 302) and resumeButtonClicked == True:
        screen.blit(asset_resume_button_clicked, (0, 0))
        resumeButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_resume_button_normal, (0, 0))
        resumeButtonHover = False

    # Settings Button -------------------------------------------------------------------------------
    # Hover Button
    if (235 <= mouse_posx <= 367) and (324 <= mouse_posy <= 370) and settingsButtonClicked == False \
            and confirmationBox == False:
        screen.blit(asset_settings_button_hover, (0, 0))
        settingsButtonHover = True
    # Click Button
    elif (235 <= mouse_posx <= 367) and (324 <= mouse_posy <= 370) and settingsButtonClicked == True:
        screen.blit(asset_settings_button_clicked, (0, 0))
        settingsButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_settings_button_normal, (0, 0))
        settingsButtonHover = False

    # Main Menu Button ------------------------------------------------------------------------------
    # Hover Button
    if (235 <= mouse_posx <= 367) and (393 <= mouse_posy <= 438) and mainMenu2ButtonClicked == False \
            and confirmationBox == False:
        screen.blit(asset_main_menu2_button_hover, (0, 0))
        mainMenu2ButtonHover = True
    # Click Button
    elif (235 <= mouse_posx <= 367) and (393 <= mouse_posy <= 438) and mainMenu2ButtonClicked == True:
        screen.blit(asset_main_menu2_button_clicked, (0, 0))
        mainMenu2ButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_main_menu2_button_normal, (0, 0))
        mainMenu2ButtonHover = False

    # Confirmation Screen --------------------------------------------------------------------------------
    if confirmationBox == True:
        screen.blit(asset_confirmation_box, (0, 0))
        # Yes --------------------------------------------------------------------------------------------
        # Hover Button
        if (189 <= mouse_posx <= 267) and (292 <= mouse_posy <= 329) and confirmYesButtonClicked == False:
            screen.blit(asset_confirm_yes_button_hover, (0, 0))
            confirmYesButtonHover = True
        # Click Button
        elif (189 <= mouse_posx <= 267) and (292 <= mouse_posy <= 329) and confirmYesButtonClicked == True:
            screen.blit(asset_confirm_yes_button_clicked, (0, 0))
            confirmYesButtonHover = False
        # Normal Button
        else:
            screen.blit(asset_confirm_yes_button_normal, (0, 0))
            confirmYesButtonHover = False
        # No --------------------------------------------------------------------------------------------
        # Hover Button
        if (333 <= mouse_posx <= 412) and (292 <= mouse_posy <= 329) and confirmNoButtonClicked == False:
            screen.blit(asset_confirm_no_button_hover, (0, 0))
            confirmNoButtonHover = True
        # Click Button
        elif (333 <= mouse_posx <= 412) and (292 <= mouse_posy <= 329) and confirmNoButtonClicked == True:
            screen.blit(asset_confirm_no_button_clicked, (0, 0))
            confirmNoButtonHover = False
        # Normal Button
        else:
            screen.blit(asset_confirm_no_button_normal, (0, 0))
            confirmNoButtonHover = False
    # Settings Menu ----------------------------------------------------------------------------------
    if settings == True:
        showSettings()


def showSettings():
    global resumeButtonHover, settingsButtonHover, mainMenu2ButtonHover, confirmYesButtonHover, \
        confirmNoButtonHover, settingsDoneButtonHover, masterLeftButtonHover, masterRightButtonHover, \
        musicLeftButtonHover, musicRightButtonHover, masterIconButtonClicked, musicIconButtonClicked, \
        masterIconButtonHover, musicIconButtonHover

    masterVolumePercent = round(masterVolume * 100)
    musicVolumePercent = round(musicVolume * 100)
    masterVolume_text = font3.render((str(masterVolumePercent) + "%"), True, (255, 255, 255))
    musicVolume_text = font3.render((str(musicVolumePercent) + "%"), True, (255, 255, 255))
    masterVolumeBack_text = font3.render((str(masterVolumePercent) + "%"), True, (18, 15, 23))
    musicVolumeBack_text = font3.render((str(musicVolumePercent) + "%"), True, (18, 15, 23))

    screen.blit(asset_settings_menu, (0, 0))
    screen.blit(masterVolumeBack_text, (406, 178))
    screen.blit(masterVolume_text, (408, 177))
    screen.blit(musicVolumeBack_text, (394, 230))
    screen.blit(musicVolume_text, (396, 229))
    # Done Button ---------------------------------------------------------------------------------
    # Hover Button
    if (235 <= mouse_posx <= 367) and (433 <= mouse_posy <= 471) and settingsDoneButtonClicked == False:
        screen.blit(asset_settings_done_button_hover, (0, 0))
        settingsDoneButtonHover = True
    # Click Button
    elif (235 <= mouse_posx <= 367) and (433 <= mouse_posy <= 471) and settingsDoneButtonClicked == True:
        screen.blit(asset_settings_done_button_clicked, (0, 0))
        settingsDoneButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_settings_done_button_normal, (0, 0))
        settingsDoneButtonHover = False
    # Master Left -----------------------------------------------------------------------------------
    # Hover Button
    if (112 <= mouse_posx <= 140) and (174 <= mouse_posy <= 204) and masterLeftButtonClicked == False and \
            masterVolumeMuted == False:
        screen.blit(asset_master_left_button_hover, (0, 0))
        masterLeftButtonHover = True
    # Click Button
    elif (112 <= mouse_posx <= 140) and (174 <= mouse_posy <= 204) and masterLeftButtonClicked == True and \
            masterVolumeMuted == False:
        screen.blit(asset_master_left_button_clicked, (0, 0))
        masterLeftButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_master_left_button_normal, (0, 0))
        masterLeftButtonHover = False
    # Master Right -----------------------------------------------------------------------------------
    # Hover Button
    if (474 <= mouse_posx <= 504) and (174 <= mouse_posy <= 204) and masterRightButtonClicked == False and \
            masterVolumeMuted == False:
        screen.blit(asset_master_right_button_hover, (0, 0))
        masterRightButtonHover = True
    # Click Button
    elif (474 <= mouse_posx <= 504) and (174 <= mouse_posy <= 204) and masterRightButtonClicked == True and \
            masterVolumeMuted == False:
        screen.blit(asset_master_right_button_clicked, (0, 0))
        masterRightButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_master_right_button_normal, (0, 0))
        masterRightButtonHover = False
    # Master Icon -----------------------------------------------------------------------------------
    # Hover Button
    if (155 <= mouse_posx <= 180) and (172 <= mouse_posy <= 206) and masterIconButtonClicked == False:
        screen.blit(asset_master_icon_button_hover, (0, 0))
        masterIconButtonHover = True
    # Click Button
    elif (155 <= mouse_posx <= 180) and (172 <= mouse_posy <= 206) and masterIconButtonClicked == True:
        screen.blit(asset_master_icon_button_clicked, (0, 0))
        masterIconButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_master_icon_button_normal, (0, 0))
        masterIconButtonHover = False
    # Music Left -----------------------------------------------------------------------------------
    # Hover Button
    if (112 <= mouse_posx <= 140) and (226 <= mouse_posy <= 257) and musicLeftButtonClicked == False and \
            musicVolumeMuted == False:
        screen.blit(asset_music_left_button_hover, (0, 0))
        musicLeftButtonHover = True
    # Click Button
    elif (112 <= mouse_posx <= 140) and (226 <= mouse_posy <= 257) and musicLeftButtonClicked == True and \
            musicVolumeMuted == False:
        screen.blit(asset_music_left_button_clicked, (0, 0))
        musicLeftButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_music_left_button_normal, (0, 0))
        musicLeftButtonHover = False
    # Music Right -----------------------------------------------------------------------------------
    # Hover Button
    if (474 <= mouse_posx <= 504) and (226 <= mouse_posy <= 257) and musicRightButtonClicked == False and \
            musicVolumeMuted == False:
        screen.blit(asset_music_right_button_hover, (0, 0))
        musicRightButtonHover = True
    # Click Button
    elif (474 <= mouse_posx <= 504) and (226 <= mouse_posy <= 257) and musicRightButtonClicked == True and \
            musicVolumeMuted == False:
        screen.blit(asset_music_right_button_clicked, (0, 0))
        musicRightButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_music_right_button_normal, (0, 0))
        musicRightButtonHover = False
    # Music Icon -----------------------------------------------------------------------------------
    # Hover Button
    if (155 <= mouse_posx <= 181) and (230 <= mouse_posy <= 258) and musicIconButtonClicked == False:
        screen.blit(asset_music_icon_button_hover, (0, 0))
        musicIconButtonHover = True
    # Click Button
    elif (155 <= mouse_posx <= 181) and (230 <= mouse_posy <= 258) and musicIconButtonClicked == True:
        screen.blit(asset_music_icon_button_clicked, (0, 0))
        musicIconButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_music_icon_button_normal, (0, 0))
        musicIconButtonHover = False
    # Master Volume Muted Strike --------------------------------------------------------------------
    if masterVolumeMuted == True:
        screen.blit(asset_volume_muted_strikethrough, (2, -53))
    # Music Volume Muted Strike ---------------------------------------------------------------------
    if musicVolumeMuted == True:
        screen.blit(asset_volume_muted_strikethrough, (0, 0))

    # volume refresh
    step.set_volume(masterVolume)
    woodstep.set_volume(masterVolume)
    button.set_volume(masterVolume)
    griprevolver.set_volume(masterVolume)
    shot.set_volume(masterVolume)
    empty.set_volume(masterVolume)
    reload.set_volume(masterVolume)
    revolverspin.set_volume(masterVolume)
    death.set_volume(masterVolume)
    playerhit.set_volume(masterVolume)
    banpain.set_volume(masterVolume)
    snipershot.set_volume(masterVolume)
    heartbeat.set_volume(masterVolume)
    breath.set_volume(masterVolume)
    door.set_volume(masterVolume)
    openbook.set_volume(masterVolume)
    turnpage.set_volume(masterVolume)
    cashregister.set_volume(masterVolume)
    error.set_volume(masterVolume)
    potion.set_volume(masterVolume)
    sniper_reload.set_volume(masterVolume)
    combatroll.set_volume(masterVolume)
    lootBody.set_volume(masterVolume)
    sawedoffshot.set_volume(masterVolume)
    sawedoffopen.set_volume(masterVolume)
    loadshell.set_volume(masterVolume)
    burp.set_volume(masterVolume)
    burp2.set_volume(masterVolume)
    burp3.set_volume(masterVolume)
    saloon_ambience.set_volume(masterVolume)
    outside_ambience.set_volume(masterVolume)
    venom_heartbeat.set_volume(masterVolume)
    rattlesnake_rattle.set_volume(masterVolume)
    rattlesnake_strike.set_volume(masterVolume)
    intromusic.set_volume(musicVolume * masterVolume)
    intro.set_volume(musicVolume * masterVolume)
    music.set_volume(musicVolume * masterVolume)
    train_distant.set_volume(masterVolume)


def showHUD():
    if displayHUD == True:
        # hp
        if poisoned == True:
            screen.blit(asset_hp_poison_icon, (11, 507))
        else:
            screen.blit(asset_hp_icon, (11, 507))
        if godMode == False:
            screen.blit(playerHP_text, (41, 505))
        elif godMode == True:
            screen.blit(infinity_text, (41, 505))

        # kills
        screen.blit(asset_kills_icon, (11, 530))
        screen.blit(playerScore_text, (41, 528))

        # money
        screen.blit(asset_money_icon, (11, 552))
        screen.blit(playerMoney_text, (41, 550))

        # ammo
        screen.blit(asset_ammo_icon, (11, 573))
        if hotbarSlot1 == True:
            screen.blit(revolverAmmo_text, (41, 571))
        elif hotbarSlot2 == True and ownSniperRifle == True:
            screen.blit(sniperAmmo_text, (41, 571))
        elif hotbarSlot3 == True and ownSawedOff == True:
            screen.blit(sawedOffAmmo_text, (41, 571))
        else:
            screen.blit(blankAmmo_text, (42, 569))

        # dev mode text
        if devMode == True:
            screen.blit(devMode_text, (width - 90, 569))

        # popup text
        if purchasedText == True:
            screen.blit(asset_text_purchased, (201, 60))
        if insufFundsText == True:
            screen.blit(asset_text_insufficient, (201, 60))
        if showWave == True:
            screen.blit(wave_text, wave_text_rect)


        # interact text
        if interactText == True and rolling == False and scopeScreen == False:
            if reloadUI == True or outAmmoUI == True:
                screen.blit(interact_text, (222, 220))
            else:
                screen.blit(interact_text, (222, 235))

        # buy text
        if buyText == True:
            screen.blit(buy_text, (137, 255))

        # ammo text
        if standing == True:
            if reloadUI == True:
                screen.blit(reload_text, (227, 235))
            if outAmmoUI == True:
                screen.blit(outAmmo_text, (215, 235))


        # hotbar
        if startGame == True and scopeScreen == False:
            screen.blit(asset_hotbar, (300 - 153.5, 560 - 28.5))
            screen.blit(asset_revolver_icon, (300 - 153.5, 560 - 28.5))
            if ownSniperRifle == True:
                screen.blit(asset_sniper_icon, (300 - 153.5, 560 - 28.5))
            if ownSawedOff == True:
                screen.blit(asset_sawed_off_icon, (300 - 153.5, 560 - 28.5))
            if hpPotionCount > 0:
                screen.blit(asset_hearty_beer_icon, (500 - 153.5, 562 - 28.5))
                screen.blit(potionCount_text, (403, 537))
            screen.blit(asset_hotbar_select, (activeSlotx1 - 3, 565 - 33))

        # loot text
        if startGame == True and insideShop == False and insideSaloon == False and standing == True:
            for bandit in Bandit.instances:
                if bandit.looted == False and bandit.stoodOn == True:
                    if (outAmmoUI or reloadUI) and interactText == True:
                        screen.blit(loot_text, (235, 205))
                    elif outAmmoUI == True or reloadUI == True or interactText == True:
                        screen.blit(loot_text, (235, 220))
                    else:
                        screen.blit(loot_text, (235, 235))

        # money gained text
        if showMoneyGainedText == True:
            screen.blit(moneyGained_text, (30, 480))


def interactCheck():
    global interactText

    # Check if in front of store
    if store1x <= 50 and store1x >= 25:
        if scopeScreen == False and insideShop == False and insideSaloon == False:
            interactText = True
    # Check if in front of saloon
    elif store2x <= 50 and store2x >= 25:
        if scopeScreen == False and insideShop == False and insideSaloon == False:
            interactText = True
    # Open Catalog
    elif store1x + 420 <= 100 and store1x + 420 >= 0:
        if playerHolster == False and playerShoot == False and insideShop == True and catalog == False \
                and playerSniper == False:
            interactText = True
    # Holding sniper rifle
    elif playerSniper == True and sniperRoundsMag > 0 and insideShop == False and insideSaloon == False:
        interactText = True
    else:
        interactText = False


def playerHit(damage):
    global playerHP, invincibility, godMode

    if playerHP > 0 and invincibility == False and godMode == False:
        playerHP -= damage
        playerHitSound_timer.start()


def venomed(ticks):
    global playerHP, invincibility, godMode, venom_ticks_remaining

    venom_ticks_remaining = ticks
    if playerHP > 0 and godMode == False:
        venomTick_timer.start()


def playerDead():
    global dead, moveAbility, startGame
    dead = True
    # death screen
    screen.blit(asset_death_screen, (300 - 300, 300 - 300))
    screen.blit(deathScore_text, (278, 250))
    screen.blit(playerHighscore_text, (264, 270))
    moveAbility = False
    startGame = False
    stopAllTimers(timerTuple)
    stopReload()
    stopSounds()
    death.stop()
    death.play()
    # Hide/Show Mouse
    pygame.mouse.set_visible(True)


def resetValues():
    global playerHP, moneyCount, revRoundsMag, revRoundsTotal, revolverFireRate, sniperRoundsMag, sniperRoundsTotal, \
        hpPotionCount, score, cloud1x, cloud2x, tumweed1x, store1x, store2x, cactusx, activeSlotx1, activeSlotx2, \
        bulletx, scopeWalk, startGame, dead, moveAbility, banMoveAbility, interactText, buyText, sitting, standing, \
        insufFundsText, purchasedText, lookingLeft, lookingRight, hotbarSlot1, hotbarSlot2, hotbarSlot3, hotbarSlot4, \
        hotbarSlot5, hotbarSlot6, reloadUI, outAmmoUI, scopeScreen,insideShop, ownSniperRifle, catalog, catalogPage1, \
        catalogPage2, catalogPage3, playerIdle, playerWalk, playerHolster, playerLegsIdle, playerShoot, playerDrink, \
        playerSniper, playerGrab, playButtonHover, playButtonClicked, readyToFireRevolver, restartButtonHover, \
        restartButtonClicked, mainMenuButtonHover, mainMenuButtonClicked, resumeButtonHover, resumeButtonClicked, \
        settingsButtonHover, settingsButtonClicked, mainMenu2ButtonHover, mainMenu2ButtonClicked, \
        confirmYesButtonHover, confirmYesButtonClicked, confirmNoButtonHover, confirmNoButtonClicked, confirmationBox, \
        settings, settingsDoneButtonHover, settingsDoneButtonClicked, masterLeftButtonHover, masterLeftButtonClicked, \
        masterRightButtonHover, masterRightButtonClicked, musicLeftButtonHover, musicLeftButtonClicked, \
        musicRightButtonHover, musicRightButtonClicked, playerRoll1Right, playerRoll2Right, playerRoll3Right, \
        playerRoll1Left, playerRoll2Left, playerRoll3Left, rolling, rollReady, cooldown_sweat_y, walkingLeft, \
        walkingRight, walkingBoth, musicIconButtonClicked, musicIconButtonHover, masterIconButtonClicked, \
        masterIconButtonHover, revolverOutAmmo, sniperOutAmmo, revolverOutMag, sniperOutMag,looting,\
        showMoneyGainedText, sawedOffRoundsMag, buckRoundsTotal,ownSawedOff,sawedOffOutMag,sawedOffOutAmmo, \
        healing, healQueue, wave, waveIntermissionLength, showWave, banditCount, venom_ticks_remaining,lastActiveSlot, \
        reloading, exitButtonHover, buyHoverP1_1, buyHoverP1_2, buyHoverP1_3, buyHoverP2_1, buyHoverP2_2, buyHoverP2_3,\
        buyHoverP2_4, poisoned, insideSaloon

    # player vals
    playerHP = 100
    moneyCount = 0
    revRoundsMag = 6
    revRoundsTotal = 24
    revolverFireRate = 120
    sniperRoundsMag = 1
    sniperRoundsTotal = 3
    sawedOffRoundsMag = 2
    buckRoundsTotal = 6
    hpPotionCount = 0
    healQueue = 0
    score = 0
    banditCount = 0
    wave = 0
    waveIntermissionLength = 1500
    venom_ticks_remaining = 0
    lastActiveSlot = 1

    # x-pos
    cloud1x = 100
    cloud2x = 600
    tumweed1x = 700
    store1x = 700
    store2x = 1400
    cactusx = 450
    cooldown_sweat_y = 252
    activeSlotx1 = -50
    activeSlotx2 = -50
    bulletx = 330

    invincibility = False
    moveAbility = True
    banMoveAbility = True
    interactText = False
    buyText = False
    sitting = False
    standing = True
    walkingRight = False
    walkingLeft = False
    walkingBoth = False
    rolling = False
    poisoned = False
    insufFundsText = False
    purchasedText = False
    lookingLeft = False
    lookingRight = True
    hotbarSlot1 = False
    hotbarSlot2 = False
    hotbarSlot3 = False
    hotbarSlot4 = False
    hotbarSlot5 = False
    hotbarSlot6 = False
    reloadUI = False
    outAmmoUI = False
    revolverOutMag = False
    sniperOutMag = False
    sawedOffOutMag = False
    revolverOutAmmo = False
    sniperOutAmmo = False
    sawedOffOutAmmo = False
    scopeScreen = False
    insideShop = False
    insideSaloon = False
    ownSniperRifle = False
    ownSawedOff = False
    catalog = False
    catalogPage1 = False
    catalogPage2 = False
    catalogPage3 = False
    playerIdle = True
    playerWalk = False
    playerHolster = False
    playerLegsIdle = True
    playerShoot = False
    playerDrink = False
    playerSniper = False
    playerGrab = False
    readyToFireRevolver = True
    playButtonHover = False
    playButtonClicked = False
    restartButtonHover = False
    mainMenuButtonHover = False
    mainMenuButtonClicked = False
    pause = False
    resumeButtonHover = False
    resumeButtonClicked = False
    settingsButtonHover = False
    settingsButtonClicked = False
    mainMenu2ButtonHover = False
    mainMenu2ButtonClicked = False
    confirmYesButtonHover = False
    confirmYesButtonClicked = False
    confirmNoButtonHover = False
    confirmNoButtonClicked = False
    confirmationBox = False
    settings = False
    settingsDoneButtonHover = False
    settingsDoneButtonClicked = False
    masterLeftButtonHover = False
    masterLeftButtonClicked = False
    masterRightButtonHover = False
    masterRightButtonClicked = False
    musicLeftButtonHover = False
    musicLeftButtonClicked = False
    musicRightButtonHover = False
    musicRightButtonClicked = False
    musicIconButtonClicked = False
    musicIconButtonHover = False
    masterIconButtonClicked = False
    masterIconButtonHover = False
    exitButtonHover = False
    playerRoll1Right = False
    playerRoll2Right = False
    playerRoll3Right = False
    playerRoll1Left = False
    playerRoll2Left = False
    playerRoll3Left = False
    rollReady = True
    looting = False
    showMoneyGainedText = False
    healing = False
    showWave = False
    reloading = False
    buyHoverP1_1 = False
    buyHoverP1_2 = False
    buyHoverP1_3 = False
    buyHoverP2_1 = False
    buyHoverP2_2 = False
    buyHoverP2_3 = False
    buyHoverP2_4 = False
    if demoMode == True:
        ownSniperRifle = True
        ownSawedOff = False
        sniperRoundsTotal = 8
        buckRoundsTotal = 16
        revRoundsTotal = 24
        hpPotionCount = 2
        moneyCount = 100

    # reset seed
    random.seed()

    # despawn bandits
    Bandit.alive = 0
    for bandit in Bandit.instances[:]:
        Bandit.instances.remove(bandit)

    # despawn rattlesnakes
    Bandit.alive = 0
    for rattlesnake in Rattlesnake.instances[:]:
        Rattlesnake.instances.remove(rattlesnake)


def stopAllTimers(tup):
    for timer in tuple(tup):
        timer.stop()


def masterVolumeDown():
    global masterVolume
    if masterVolume > 0.1:
        masterVolume = masterVolume - 0.1


def masterVolumeUp():
    global masterVolume
    if masterVolume < 1:
        masterVolume = masterVolume + 0.1


def masterVolumeMute(previous_volume):
    global masterVolume, masterVolumeMuted
    if masterVolumeMuted == True:
        masterVolume = previous_volume
        masterVolumeMuted = False
    elif masterVolumeMuted == False:
        masterVolume = 0
        masterVolumeMuted = True


def musicVolumeDown():
    global musicVolume
    if musicVolume > 0.1:
        musicVolume = musicVolume - 0.1


def musicVolumeUp():
    global musicVolume
    if musicVolume < 1:
        musicVolume = musicVolume + 0.1


def musicVolumeMute(previous_volume):
    global musicVolume, musicVolumeMuted
    if musicVolumeMuted == True:
        musicVolume = previous_volume
        musicVolumeMuted = False
    elif musicVolumeMuted == False:
        musicVolume = 0
        musicVolumeMuted = True


def switchSlots(slot):
    global hotbarSlot1,hotbarSlot2,hotbarSlot3,hotbarSlot4,hotbarSlot5,hotbarSlot6,playerHolster,playerIdle,reloadUI, \
        playerShoot, playerSniper, interactText, playerGrab, outAmmoUI,lastActiveSlot
    if slot == 1:
        hotbarSlot1 = not hotbarSlot1
        hotbarSlot2 = False
        hotbarSlot3 = False
        hotbarSlot4 = False
        hotbarSlot5 = False
        hotbarSlot6 = False
        lastActiveSlot = 1
        stopReload()
        griprevolver.stop()
        griprevolver.play()
        playerHolster = True
        playerShoot = False
        playerIdle = False
        playerSniper = False
        if hotbarSlot1 == False:
            playerShoot = False
            playerHolster = False
            playerIdle = True
        if insideShop == True or insideSaloon == True:
            interactText = False

    elif slot == 2:
        if scopeScreen == False:
            hotbarSlot2 = not hotbarSlot2
            hotbarSlot1 = False
            hotbarSlot3 = False
            hotbarSlot4 = False
            hotbarSlot5 = False
            hotbarSlot6 = False
            lastActiveSlot = 2
            playerHolster = False
            playerShoot = False
            stopReload()
            if ownSniperRifle == True:
                playerSniper = not playerSniper
                playerGrab = True
                griprevolver.stop()
                griprevolver.play()
                playerIdle = False
            if insideShop == True or insideSaloon == True:
                interactText = False
    elif slot == 3:
        hotbarSlot1 = False
        hotbarSlot2 = False
        hotbarSlot3 = not hotbarSlot3
        hotbarSlot4 = False
        hotbarSlot5 = False
        hotbarSlot6 = False
        lastActiveSlot = 3
        interactText = False
        playerHolster = False
        playerSniper = False
        playerShoot = False
        stopReload()
        if ownSawedOff == True:
            playerHolster = True
            playerIdle = False
            griprevolver.stop()
            griprevolver.play()
        if hotbarSlot3 == False:
            playerShoot = False
            playerHolster = False
            playerIdle = True

    elif slot == 4:
        hotbarSlot1 = False
        hotbarSlot2 = False
        hotbarSlot3 = False
        hotbarSlot4 = not hotbarSlot4
        hotbarSlot5 = False
        hotbarSlot6 = False
        lastActiveSlot = 4
        interactText = False
        playerSniper = False
        playerHolster = False
        stopReload()
    elif slot == 5:
        hotbarSlot5 = not hotbarSlot5
        hotbarSlot1 = False
        hotbarSlot2 = False
        hotbarSlot3 = False
        hotbarSlot4 = False
        hotbarSlot6 = False
        lastActiveSlot = 5
        interactText = False
        playerSniper = False
        playerHolster = False
        stopReload()
    elif slot == 6:
        hotbarSlot6 = not hotbarSlot6
        hotbarSlot1 = False
        hotbarSlot2 = False
        hotbarSlot3 = False
        hotbarSlot4 = False
        hotbarSlot5 = False
        lastActiveSlot = 6
        stopReload()
        interactText = False
        playerHolster = False
        playerSniper = False
        playerShoot = False


# scrolls to right slot
def nextSlot():
    global hotbarSlot1, hotbarSlot2, hotbarSlot3, hotbarSlot4, hotbarSlot5, hotbarSlot6
    if hotbarSlot1:
        switchSlots(2)
    elif hotbarSlot2:
        switchSlots(3)
    elif hotbarSlot3:
        switchSlots(4)
    elif hotbarSlot4:
        switchSlots(5)
    elif hotbarSlot5:
        switchSlots(6)
    elif hotbarSlot6:
        switchSlots(1)


# scrolls to left slot
def prevSlot():
    global hotbarSlot1, hotbarSlot2, hotbarSlot3, hotbarSlot4, hotbarSlot5, hotbarSlot6
    if hotbarSlot1:
        switchSlots(6)
    elif hotbarSlot2:
        switchSlots(1)
    elif hotbarSlot3:
        switchSlots(2)
    elif hotbarSlot4:
        switchSlots(3)
    elif hotbarSlot5:
        switchSlots(4)
    elif hotbarSlot6:
        switchSlots(5)


def holsterSlot():
    global hotbarSlot1, hotbarSlot2, hotbarSlot3, hotbarSlot4, hotbarSlot5, hotbarSlot6, lastActiveSlot
    if lastActiveSlot == 1:
        switchSlots(1)
    elif lastActiveSlot == 2:
        switchSlots(2)
    elif lastActiveSlot == 3:
        switchSlots(3)
    elif lastActiveSlot == 4:
        switchSlots(4)
    elif lastActiveSlot == 5:
        switchSlots(5)
    elif lastActiveSlot == 6:
        switchSlots(6)


def exitGame():
    global devMode, demoMode
    # save highscore to file
    if devMode == False or demoMode == True:
        pickle_out = open("savedata/highscore.txt", "wb")
        pickle.dump(highscore, pickle_out)
        pickle_out.close()
    # close game
    pygame.mixer.stop()
    music_timer.stop()
    stopAllTimers(timerTuple)
    pygame.quit()
    sys.exit()


def stopReload():
    global reloading
    revolver_reload_timer.stop()
    sniper_reload_timer.stop()
    sawed_off_reload_timer.stop()
    reload.stop()
    revolverspin.stop()
    sniper_reload.stop()
    sawedoffopen.stop()
    loadshell.stop()
    reloading = False


def waveHandler(wave_num):
    global wave, waveIntermissionLength, showWave, banditCount, snakeCount
    # starting wave
    if wave_num == 0:
        wave += 1
        banditCount += 1
        showWave_timer.start()
        Bandit()
    # all other waves
    if wave_num > 0:
        wave += 1
        # every 2 waves, incrememnt amount of bandits by 1
        if wave % 2 == 1:
            banditCount += 1
        # every 5 waves, incrememnt amount of rattlesnakes by 1
        if wave % 5 == 0:
            snakeCount += 1
        # increase intermission length by 3 seconds
        waveIntermissionLength += 3000
        # show wave number
        showWave_timer.start()
        for i in range(0, banditCount):
            Bandit()
        for i in range(0, snakeCount):
            Rattlesnake()



def volumeButtonReset_timer_handler():
    global masterRightButtonClicked, musicRightButtonClicked, masterLeftButtonClicked, musicLeftButtonClicked, \
        masterIconButtonClicked, musicIconButtonClicked
    masterLeftButtonClicked = False
    musicLeftButtonClicked = False
    masterRightButtonClicked = False
    musicRightButtonClicked = False
    masterIconButtonClicked = False
    musicIconButtonClicked = False


def revolver_reload_timer_handler():
    global revRoundsMag, revRoundsTotal
    if revRoundsTotal > 0:
        revRoundsTotal -= 1
        revRoundsMag += 1
    if revRoundsMag == 6 or revRoundsTotal == 0:
        reloadEnded_timer.start()
        revolver_reload_timer.stop()


def sniper_reload_timer_handler():
    global sniperRoundsMag, sniperRoundsTotal, reloading
    if sniperRoundsTotal > 0:
        sniperRoundsTotal -= 1
        sniperRoundsMag += 1
    if sniperRoundsMag == 1:
        reloading = False
        sniper_reload_timer.stop()


def sawed_off_reload_timer_handler():
    global sawedOffRoundsMag, buckRoundsTotal
    if buckRoundsTotal > 0:
        buckRoundsTotal -= 1
        sawedOffRoundsMag += 1
        loadshell.stop()
        loadshell.play()
    if sawedOffRoundsMag == 2 or buckRoundsTotal == 0:
        sawedOffreloadEnded_timer.start()
        sawed_off_reload_timer.stop()


def music_timer_handler():
    global music
    music.play()
    music_timer.stop()


def startGame_timer_handler():
    global tumbleAuto, moveAbility, banMoveAbility, startGame, dead, restartButtonClicked,playButtonClicked
    tumbleAuto = 15
    startGame = True
    dead = False
    playButtonClicked = False
    restartButtonClicked = False
    moveAbility = True
    banMoveAbility = True
    trainDistantCooldown_timer.start()
    outside_ambience.play(-1)
    music_timer.start()
    startGame_timer.stop()


def mainMenu_timer_handler():
    global startGame, dead, mainMenuButtonClicked, mainMenu2ButtonClicked, pause
    startGame = False
    dead = False
    resetValues()
    mainMenuButtonClicked = False
    mainMenu2ButtonClicked = False
    pause = False
    mainMenu()
    intromusic.play(-1)
    mainMenu_timer.stop()


def settingsMenu_timer_handler():
    global settingsButtonClicked, settings
    settings = True
    settingsButtonClicked = False
    settingsMenu_timer.stop()


def settingsDone_timer_handler():
    global settingsDoneButtonClicked, settings
    settings = False
    settingsDoneButtonClicked = False
    settingsDone_timer.stop()


def resumeGame_timer_handler():
    global pause, resumeButtonClicked, confirmationBox, settings
    pause = False
    settings = False
    confirmationBox = False
    resumeButtonClicked = False
    pygame.mixer.unpause()
    resumeGame_timer.stop()


def revolverFireDelay_timer_handler():
    global readyToFireRevolver
    readyToFireRevolver = True
    revolverFireDelay_timer.stop()


def drinkResetDelay_timer_handler():
    global playerDrink
    playerDrink = False
    drinkResetDelay_timer.stop()


def playerHitSound_timer_handler():
    global playerHP
    if playerHP > 0:
        playerhit.play()
        playerHitSound_timer.stop()
    else:
        playerHitSound_timer.stop()


def confirmationBox_timer_handler():
    global confirmationBox, mainMenu2ButtonClicked
    confirmationBox = True
    mainMenu2ButtonClicked = False
    confirmationBox_timer.stop()


def rollStart_timer_handler():
    global standing, rolling, playerRoll1Left, playerRoll2Left, playerRoll3Left, playerRoll1Right, interactText,\
        playerRoll2Right, playerRoll3Right,invincibility, rollReady, cooldown_sweat_y,playerShoot, scopeScreen, \
        insideShop, store1x,store2x, cactusx, banMoveAbility, moveAbility,insideSaloon
    standing = False
    rolling = True
    invincibility = True
    playerShoot = False
    scopeScreen = False
    rollReady = False
    cooldown_sweat_y = 252
    disableText()
    combatroll.play()
    if lookingRight == True:
        playerRoll1Right = True
        if insideShop == True:
            if (store1x + 700) <= 0:
                worldRight(0)
                moveAbility = False
            else:
                worldRight(1)
        elif insideSaloon == True:
            if (store2x + 700) <= 0:
                worldRight(0)
                moveAbility = False
        else:
            worldRight(1)
    elif lookingLeft == True:
        if insideShop == True:
            if (store1x - 200) >= 0:
                insideShop = False
                store1x = 50
                store2x = 750
                cactusx = -200
                banMoveAbility = True
                door.stop()
                door.play()
                outside_ambience.play(-1)
        elif insideSaloon == True:
            if (store2x - 200) >= 0:
                insideSaloon = False
                store1x = -650
                store2x = 50
                cactusx = -900
                banMoveAbility = True
                door.stop()
                door.play()
                outside_ambience.play(-1)
        playerRoll1Left = True
        worldLeft(1)
    rollMid1_timer.start()
    rollStart_timer.stop()


def rollMid1_timer_handler():
    global standing, rolling, playerRoll1Left, playerRoll2Left, playerRoll1Right, playerRoll2Right, \
        playerRoll3Right,playerRoll3Left, insideShop, store1x,store2x, cactusx, banMoveAbility, moveAbility,insideSaloon
    if lookingRight == True:
        playerRoll1Right = False
        playerRoll2Right = True
        if insideShop == True:
            if (store1x + 700) <= 0:
                worldRight(0)
                moveAbility = False
            else:
                worldRight(1)
        elif insideSaloon == True:
            if (store2x + 700) <= 0:
                worldRight(0)
                moveAbility = False
            else:
                worldRight(1)
        else:
            worldRight(1)
    elif lookingLeft == True:
        if insideShop == True:
            if (store1x - 200) >= 0:
                insideShop = False
                store1x = 50
                store2x = 750
                cactusx = -200
                banMoveAbility = True
                door.stop()
                door.play()
                outside_ambience.play(-1)
        elif insideSaloon == True:
            if (store2x - 200) >= 0:
                insideSaloon = False
                store1x = -650
                store2x = 50
                cactusx = -900
                banMoveAbility = True
                door.stop()
                door.play()
                outside_ambience.play(-1)
        playerRoll1Left = False
        playerRoll2Left = True
        worldLeft(1)
    rollMid2_timer.start()
    rollMid1_timer.stop()


def rollMid2_timer_handler():
    global standing, rolling, playerRoll1Left, playerRoll2Left, playerRoll1Right, playerRoll2Right,\
        playerRoll3Right,playerRoll3Left, moveAbility, insideSaloon,insideShop,store1x, store2x
    if lookingRight == True:
        playerRoll2Right = False
        playerRoll3Right = True
        if insideShop == True:
            if (store1x + 700) <= 0:
                worldRight(0)
                moveAbility = False
            else:
                worldRight(1)
        elif insideSaloon == True:
            if (store2x + 700) <= 0:
                worldRight(0)
                moveAbility = False
            else:
                worldRight(1)
        else:
            worldRight(1)
    elif lookingLeft == True:
        playerRoll2Left = False
        playerRoll3Left = True
        worldLeft(1)
    rollEnd_timer.start()
    rollMid2_timer.stop()


def rollEnd_timer_handler():
    global standing, rolling, playerRoll1Left, playerRoll2Left, playerRoll1Right, playerRoll2Right, \
        playerRoll3Right, invincibility,interactText,playerRoll3Left, moveAbility, insideShop, store1x,store2x,\
        cactusx, banMoveAbility, moveAbility, insideSaloon
    if lookingRight == True:
        playerRoll1Right = False
        playerRoll2Right = False
        playerRoll3Right = False
        if insideShop == True:
            if (store1x + 700) <= 0:
                worldRight(0)
                moveAbility = False
            else:
                worldRight(1)
            # fixes bug where you can roll then walk through wall
            if (store1x + 700) <= 0:
                moveAbility = False
        elif insideSaloon == True:
            if (store2x + 700) <= 0:
                worldRight(0)
                moveAbility = False
            else:
                worldRight(1)
            # fixes bug where you can roll then walk through wall
            if (store2x + 700) <= 0:
                moveAbility = False
        else:
            worldRight(1)
    elif lookingLeft == True:
        if insideShop == True:
            if (store1x - 200) >= 0:
                insideShop = False
                store1x = 50
                store2x = 750
                cactusx = -200
                banMoveAbility = True
                door.stop()
                door.play()
                outside_ambience.play(-1)
        elif insideSaloon == True:
            if (store2x - 200) >= 0:
                insideSaloon = False
                store1x = -650
                store2x = 50
                cactusx = -900
                banMoveAbility = True
                door.stop()
                door.play()
                outside_ambience.play(-1)
        playerRoll1Left = False
        playerRoll2Left = False
        playerRoll3Left = False
        worldLeft(1)
    standing = True
    rolling = False
    invincibility = False
    rollCooldown_timer.start()
    rollEnd_timer.stop()


def rollCooldown_timer_handler():
    global rollReady
    rollReady = True
    rollCooldown_timer.stop()


def walk1_timer_handler():
    ## Continuous walking function, called when press A or D or by walk2_timer if player holds A or D

    # start walk2_timer
    walk2_timer.start()
    walk1_timer.stop()


def walk2_timer_handler():
    ## Continuous walking function, if A or D is still being held, walk again and loop back to walk1_timer
    ## Allows the player to continuously walk when holding down keys, loop breaks when player releases keys

    if lookingRight:
        # if player is still holding down walk right key
        # 'and not' prevents bug where player repeatedly walks left and right if both are held
        if walkingRight and not walkingLeft:
            walkRight()
            walk1_timer.start()
    elif lookingLeft:
        # if player is still holding down walk left key
        # 'and not' prevents bug where player repeatedly walks left and right if both are held
        if walkingLeft and not walkingRight:
            walkLeft()
            walk1_timer.start()
    walk2_timer.stop()


def reloadEnded_timer_handler():
    global reloading
    reload.stop()
    revolverspin.play()
    reloading = False
    reloadEnded_timer.stop()


def sawedOffreloadEnded_timer_handler():
    global reloading
    sawedoffopen.stop()
    sawedoffopen.play()
    reloading = False
    sawedOffreloadEnded_timer.stop()


def loot_timer_handler():
    global looting, standing, moveAbility
    looting = False
    standing = True
    moveAbility = True
    loot_timer.stop()


def showMoneyGained_timer_handler():
    global showMoneyGainedText
    showMoneyGainedText = False
    showMoneyGained_timer.stop()


def burp_timer_handler():
    # common burp rarity
    x = random.randint(1,5)
    # rare burp rarity
    y = random.randint(1,25)
    # legendary burp rarity
    z = random.randint(1, 1000)
    if z == 1:
        burp3.play()
    elif y == 1:
        burp2.play()
    elif x == 1:
        burp.play()
    burp_timer.stop()


def beerHealing_timer_handler():
    global playerHP, healing, healQueue
    # loops until playerHP is 100 or until healQueue is down to 0
    if playerHP < 100 and healQueue > 0:
        playerHP += 1
        healQueue -= 1
        healing = True
        beerHealing_timer.start()
    else:
        healQueue = 0
        healing = False
        beerHealing_timer.stop()


def startWave_timer_handler():
    waveHandler(wave)
    startWave_timer.stop()


def showWave_timer_handler():
    global showWave
    showWave = True
    hideWave_timer.start()
    showWave_timer.stop()


def hideWave_timer_handler():
    global showWave
    showWave = False
    hideWave_timer.stop()


def venomTick_timer_handler():
    global playerHP, venom_ticks_remaining, poisoned

    if venom_ticks_remaining > 0:
        if playerHP > 0 and godMode == False and pause == False:
            poisoned = True
            playerHP -= 2
            venom_heartbeat.play()
            venom_ticks_remaining -= 1
            venomTick_timer.start()
    elif venom_ticks_remaining == 0:
        poisoned = False
        venomTick_timer.stop()


def snakeStrikeStop_timer_handler():
    for rattlesnake in Rattlesnake.instances:
        if rattlesnake.striking == True:
            rattlesnake.striking = False
    snakeStrikeStop_timer.stop()


def snakeStrikeCooldown_timer_handler():
    for rattlesnake in Rattlesnake.instances:
        if rattlesnake.strikeCooldown == True:
            rattlesnake.strikeCooldown = False
    snakeStrikeCooldown_timer.stop()


def snakeRattleCooldown_timer_handler():
    for rattlesnake in Rattlesnake.instances:
        if rattlesnake.rattleCooldown == True:
            rattlesnake.rattleCooldown = False
    snakeRattleCooldown_timer.stop()


def snakeRattleSoundCooldown_timer_handler():
    for rattlesnake in Rattlesnake.instances:
        if rattlesnake.rattleSoundCooldown == True:
            rattlesnake.rattleSoundCooldown = False
    snakeRattleSoundCooldown_timer.stop()


def trainDistantCooldown_timer_handler():
    train_distant.play()
    trainDistantCooldown_timer.start()


# timers (ms, timer_handler) (1000ms = 1sec)
revolver_reload_timer = simplegui.create_timer(revolverReloadSpeed, revolver_reload_timer_handler)
sniper_reload_timer = simplegui.create_timer(1000, sniper_reload_timer_handler)
sawed_off_reload_timer = simplegui.create_timer(500, sawed_off_reload_timer_handler)
music_timer = simplegui.create_timer(15000, music_timer_handler)
startGame_timer = simplegui.create_timer(50, startGame_timer_handler)
mainMenu_timer = simplegui.create_timer(50, mainMenu_timer_handler)
settingsMenu_timer = simplegui.create_timer(50, settingsMenu_timer_handler)
settingsDone_timer = simplegui.create_timer(50, settingsDone_timer_handler)
volumeButtonReset_timer = simplegui.create_timer(50, volumeButtonReset_timer_handler)
resumeGame_timer = simplegui.create_timer(50, resumeGame_timer_handler)
confirmationBox_timer = simplegui.create_timer(50, confirmationBox_timer_handler)
revolverFireDelay_timer = simplegui.create_timer(revolverFireRate, revolverFireDelay_timer_handler)
drinkResetDelay_timer = simplegui.create_timer(drinkTime, drinkResetDelay_timer_handler)
playerHitSound_timer = simplegui.create_timer(100, playerHitSound_timer_handler)
rollStart_timer = simplegui.create_timer(1, rollStart_timer_handler)
rollMid1_timer = simplegui.create_timer(75, rollMid1_timer_handler)
rollMid2_timer = simplegui.create_timer(75, rollMid2_timer_handler)
rollEnd_timer = simplegui.create_timer(75, rollEnd_timer_handler)
rollCooldown_timer = simplegui.create_timer(1500, rollCooldown_timer_handler)
walk1_timer = simplegui.create_timer(1, walk1_timer_handler)
walk2_timer = simplegui.create_timer(150, walk2_timer_handler)
reloadEnded_timer = simplegui.create_timer(125, reloadEnded_timer_handler)
sawedOffreloadEnded_timer = simplegui.create_timer(500, sawedOffreloadEnded_timer_handler)
loot_timer = simplegui.create_timer(200, loot_timer_handler)
showMoneyGained_timer = simplegui.create_timer(2000, showMoneyGained_timer_handler)
burp_timer = simplegui.create_timer(1000, burp_timer_handler)
beerHealing_timer = simplegui.create_timer(beerRegenRate, beerHealing_timer_handler)
startWave_timer = simplegui.create_timer(waveIntermissionLength, startWave_timer_handler)
showWave_timer = simplegui.create_timer(100, showWave_timer_handler)
hideWave_timer = simplegui.create_timer(3000, hideWave_timer_handler)
venomTick_timer = simplegui.create_timer(1000, venomTick_timer_handler)
snakeStrikeStop_timer = simplegui.create_timer(200, snakeStrikeStop_timer_handler)
snakeStrikeCooldown_timer = simplegui.create_timer(3000, snakeStrikeCooldown_timer_handler)
snakeRattleCooldown_timer = simplegui.create_timer(5, snakeRattleCooldown_timer_handler)
snakeRattleSoundCooldown_timer = simplegui.create_timer(3200, snakeRattleSoundCooldown_timer_handler)
trainDistantCooldown_timer = simplegui.create_timer(120000, trainDistantCooldown_timer_handler)



# timers tuple
timerTuple = (trainDistantCooldown_timer, revolver_reload_timer, sniper_reload_timer, music_timer, startGame_timer,
              revolverFireDelay_timer, drinkResetDelay_timer, resumeGame_timer, mainMenu_timer, playerHitSound_timer,
              confirmationBox_timer, volumeButtonReset_timer, settingsDone_timer, settingsMenu_timer, rollStart_timer,
              rollMid1_timer, rollEnd_timer, rollCooldown_timer, walk1_timer, walk2_timer, reloadEnded_timer, loot_timer,
              showMoneyGained_timer, sawed_off_reload_timer, sawedOffreloadEnded_timer,burp_timer, beerHealing_timer,
              startWave_timer, hideWave_timer, showWave_timer, venomTick_timer, snakeStrikeStop_timer,
              snakeStrikeCooldown_timer, snakeRattleCooldown_timer, snakeRattleSoundCooldown_timer)

# Main Menu Music
intromusic.play(-1)
intromusic.set_volume(masterVolume*musicVolume)
resetValues()
# Hide/Show Mouse
pygame.mouse.set_visible(True)

# load highscore from file
try:
    pickle_in = open("savedata/highscore.txt","rb")
    highscore = pickle.load(pickle_in)
    pickle_in.close()
except:
    pickle_out = open("savedata/highscore.txt", "wb")
    pickle.dump(highscore, pickle_out)
    pickle_out.close()

if demoMode == True:
    resetValues()

# Game Loop (Screen Refresh Loop)
while True:
    # Event Handler ------------------------------------------------------------------------------------------
    for event in pygame.event.get():
        # When game is closed
        if event.type == pygame.QUIT:
            exitGame()
        # Check Walk Both (Fixes bug where player gets stuck when switching directions)
        checkWalkBoth()
        # Key Down Handler
        if event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            # Developer Tools
            if devMode == True:
                # god mode
                if event.key == pygame.K_g and mods & pygame.KMOD_CTRL:
                    godMode = not godMode
                    potion.play()
                # invisible mode
                if event.key == pygame.K_h and mods & pygame.KMOD_CTRL:
                    invisible = not invisible
                    potion.play()
                # spawn bandit
                if event.key == pygame.K_b and mods & pygame.KMOD_CTRL:
                    ban = Rattlesnake(400)
                    button.play()
                # give ammo
                if event.key == pygame.K_n and mods & pygame.KMOD_CTRL:
                    revRoundsTotal += 1000
                    sniperRoundsTotal += 1000
                    buckRoundsTotal += 1000
                    revolverspin.play()
                # give money
                if event.key == pygame.K_m and mods & pygame.KMOD_CTRL:
                    giveMoney(10000)
                    cashregister.play()
                if event.key == pygame.K_f and mods & pygame.KMOD_CTRL:
                    resetValues()
                    potion.play()
            # Enable Cheats
            if event.key == pygame.K_o and mods & pygame.KMOD_CTRL:
                devMode = True
                burp2.play()
            # Hide HUD
            if event.key == pygame.K_u and mods & pygame.KMOD_CTRL:
                displayHUD = not displayHUD

            # Pause Game
            if event.key == pygame.K_ESCAPE and pause == False and startGame == True and dead == False:
                pygame.mixer.pause()
                screen.blit(asset_paused_darken, (0, 0))
                pause = True
                # Hide/Show Mouse
                pygame.mouse.set_visible(True)

            # Unpause Game
            elif event.key == pygame.K_ESCAPE and pause == True and settings == False:
                resumeGame_timer.start()
                # Hide/Show Mouse
                pygame.mouse.set_visible(False)

            # Exit settings
            elif event.key == pygame.K_ESCAPE and settings == True:
                settings = False
                # Hide/Show Mouse
                pygame.mouse.set_visible(False)

            if pause == False:
                # Walk left
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    walkLeft()
                    # stop timers to prevent walk timer stack bug
                    walk2_timer.stop()
                    walk1_timer.stop()
                    walkingLeft = True
                    walk1_timer.start()

                # Walk right
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    walkRight()
                    # stop timers to prevent walk timer stack bug
                    walk2_timer.stop()
                    walk1_timer.stop()
                    walkingRight = True
                    walk1_timer.start()

                # Roll
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    roll()

                # Reloading
                if event.key == pygame.K_r:
                    # Revolver
                    if hotbarSlot1 == True:
                        if revRoundsMag < 6:
                            playerHolster = True
                            playerShoot = False
                            if revRoundsTotal > 0 and reloading == False:
                                reloading = True
                                reload.stop()
                                reload.play()
                                revolver_reload_timer.start()
                    # Sniper Rifle
                    if hotbarSlot2 == True or scopeScreen == True:
                        if sniperRoundsMag < 1:
                            scopeScreen = False
                            playerSniper = True
                            if sniperRoundsTotal > 0 and reloading == False:
                                reloading = True
                                sniper_reload.stop()
                                sniper_reload.play()
                                sniper_reload_timer.start()
                    # Sawed Off
                    if hotbarSlot3 == True:
                        if sawedOffRoundsMag < 2:
                            playerHolster = True
                            playerShoot = False
                            if buckRoundsTotal > 0 and reloading == False:
                                reloading = True
                                sawedoffopen.stop()
                                sawedoffopen.play()
                                sawed_off_reload_timer.start()

                # Use Item (Space)
                if event.key == pygame.K_SPACE:
                    if pause == False and dead == False and rolling == False:
                        # Revolver fire
                        if hotbarSlot1 == True:
                            if moveAbility == True and readyToFireRevolver == True:
                                if revRoundsMag > 0:
                                    fire()
                                    readyToFireRevolver = False
                                    revolverFireDelay_timer.start()
                                else:
                                    playerShoot = True
                                    playerHolster = False
                                    empty.stop()
                                    empty.play()
                        # Sniper Rifle fires
                        if hotbarSlot2 == True and ownSniperRifle == True and scopeScreen == True:
                            if sniperRoundsMag > 0:
                                fire()
                            else:
                                empty.stop()
                                empty.play()
                        # Sawed-Off fires
                        if hotbarSlot3 == True and ownSawedOff == True:
                            if sawedOffRoundsMag > 0:
                                fire()
                            else:
                                playerShoot = True
                                playerHolster = False
                                empty.stop()
                                empty.play()
                        # HP Potion is used
                        if hotbarSlot6 == True and hpPotionCount > 0 and playerDrink == False:
                            hpPotion()

                # Aim Sniper Rifle
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if hotbarSlot2 == True and playerSniper == True and ownSniperRifle == True \
                            and insideShop == False and insideSaloon == False and rolling == False and looting == False:
                        scopeScreen = not scopeScreen
                        if scopeScreen == True:
                            breath.stop()
                            breath.play()
                            heartbeat.stop()
                            heartbeat.play(-1)

                # Loot body
                if event.key == pygame.K_f and rolling == False and insideShop == False and insideSaloon == False:
                    for bandit in Bandit.instances:
                        if bandit.looted == False and bandit.stoodOn:
                            bandit.looted = True
                            loot()

                # Hotbar slots
                if moveAbility == True and looting == False:
                    # Switch to hotbar slot 1
                    if event.key == pygame.K_1 and scopeScreen == False:
                        switchSlots(1)
                    # Switch to hotbar slot 2
                    if event.key == pygame.K_2:
                        switchSlots(2)
                    # Switch to hotbar slot 3
                    if event.key == pygame.K_3 and scopeScreen == False:
                        switchSlots(3)
                    # Switch to hotbar slot 4
                    if event.key == pygame.K_4 and scopeScreen == False:
                        switchSlots(4)
                    # Switch to hotbar slot 5
                    if event.key == pygame.K_5 and scopeScreen == False:
                        switchSlots(5)
                    # Switch to hotbar slot Q (6)
                    if event.key == pygame.K_q and scopeScreen == False:
                        switchSlots(6)

                    if event.key == pygame.K_t and scopeScreen == False:
                        holsterSlot()

                # Enter Store
                if store1x <= 50 and store1x >= 25:
                    if scopeScreen == False and insideShop == False and insideSaloon == False and playerSniper == False:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            insideShop = True
                            lookingRight = True
                            lookingLeft = False
                            interactText = False
                            banMoveAbility = False
                            walkRight()
                            # offset on screen bandits
                            for bandit in Bandit.instances:
                                # if on screen
                                if bandit.x_location >= -120 and bandit.x_location <= 600 and bandit.hp > 0:
                                    # if to the left
                                    if bandit.x_location <= 250:
                                        bandit.x_location -= 400
                                    # if to the right
                                    elif bandit.x_location > 250:
                                        bandit.x_location += 350
                            store1x = 150
                            store2x = 850
                            cactusx = -100
                            door.stop()
                            door.play()
                            outside_ambience.stop()

                # Enter Saloon
                if store2x <= 50 and store2x >= 25:
                    if scopeScreen == False and insideSaloon == False and insideShop == False and playerSniper == False:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            insideSaloon = True
                            lookingRight = True
                            lookingLeft = False
                            interactText = False
                            banMoveAbility = False
                            walkRight()
                            # offset on screen bandits
                            for bandit in Bandit.instances:
                                # if on screen
                                if bandit.x_location >= -120 and bandit.x_location <= 600 and bandit.hp > 0:
                                    # if to the left
                                    if bandit.x_location <= 250:
                                        bandit.x_location -= 400
                                    # if to the right
                                    elif bandit.x_location > 250:
                                        bandit.x_location += 350
                            store1x = -550
                            store2x = 150
                            cactusx = -800
                            door.stop()
                            door.play()
                            outside_ambience.stop()
                            saloon_ambience.play(-1)

                # Open Catalog
                if store1x + 420 <= 100 and store1x + 420 >= 0:
                    if playerHolster == False and playerShoot == False and insideShop == True and catalog == False\
                            and playerSniper == False:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            catalog = not catalog
                            catalogPage1 = True
                            interactText = False
                            moveAbility = False
                            disableText()
                            openbook.stop()
                            openbook.play()
                            # Hide/Show Mouse
                            pygame.mouse.set_visible(True)
                    elif playerHolster == False and playerShoot == False and insideShop == True and catalog == True\
                            and playerSniper == False:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            # Hide/Show Mouse
                            pygame.mouse.set_visible(False)
                            catalog = False
                            catalogPage1 = False
                            catalogPage2 = False
                            catalogPage3 = False
                            disableText()
                            moveAbility = True
                            openbook.stop()
                            openbook.play()
                # Turn Pages
                if catalog == True:
                    if catalogPage1 == True:
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            catalogPage1 = False
                            catalogPage2 = True
                            catalogPage3 = False
                            disableText()
                            turnpage.play()
                    elif catalogPage2 == True:
                        # Purchase Sniper Rifle
                        if event.key == pygame.K_2:
                            if moneyCount >= 1000 and ownSniperRifle == False:
                                purchasedText = True
                                insufFundsText = False
                                ownSniperRifle = True
                                hotbarSlot2 = False
                                moneyCount -= 1000
                                cashregister.play()
                            elif moneyCount < 1000 and ownSniperRifle == False:
                                insufFundsText = True
                                error.play()
                        # Purchase Sawed Off
                        if event.key == pygame.K_3:
                            if moneyCount >= 3000 and ownSawedOff == False:
                                purchasedText = True
                                insufFundsText = False
                                ownSawedOff = True
                                hotbarSlot3 = False
                                moneyCount -= 3000
                                cashregister.play()
                            elif moneyCount < 3000 and ownSawedOff == False:
                                insufFundsText = True
                                error.play()
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            catalogPage1 = False
                            catalogPage2 = False
                            catalogPage3 = True
                            disableText()
                            turnpage.play()
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            catalogPage1 = True
                            catalogPage2 = False
                            catalogPage3 = False
                            disableText()
                            turnpage.play()
                    elif catalogPage3 == True:
                        # Purchase Revolver Rounds
                        if event.key == pygame.K_1:
                            if moneyCount >= 50:
                                insufFundsText = False
                                purchasedText = True
                                revRoundsTotal += 24
                                moneyCount -= 50
                                cashregister.play()
                            elif moneyCount < 50:
                                purchasedText = False
                                insufFundsText = True
                                error.play()
                        # Purchase Sniper Rifle Rounds
                        if event.key == pygame.K_2:
                            if moneyCount >= 100:
                                insufFundsText = False
                                purchasedText = True
                                sniperRoundsTotal += 6
                                moneyCount -= 100
                                cashregister.play()
                            elif moneyCount < 100:
                                purchasedText = False
                                insufFundsText = True
                                error.play()
                        # Purchase 12 Gauge Shells1
                        if event.key == pygame.K_3:
                            if moneyCount >= 100:
                                insufFundsText = False
                                purchasedText = True
                                buckRoundsTotal += 12
                                moneyCount -= 100
                                cashregister.play()
                            elif moneyCount < 100:
                                purchasedText = False
                                insufFundsText = True
                                error.play()
                        # Purchase HP Potion
                        if event.key == pygame.K_4:
                            if moneyCount >= 100:
                                insufFundsText = False
                                purchasedText = True
                                hpPotionCount += 1
                                moneyCount -= 100
                                cashregister.play()
                            elif moneyCount < 100:
                                purchasedText = False
                                insufFundsText = True
                                error.play()
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            catalogPage1 = False
                            catalogPage2 = True
                            catalogPage3 = False
                            disableText()
                            turnpage.play()
        # Key Up Handler
        if event.type == pygame.KEYUP:
            # Let go of walk left
            if walkingBoth == False and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                walkingLeft = False
                walk2_timer.stop()
                walk1_timer.stop()
            # Let go of walk left while holding both
            elif walkingBoth == True and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                walk2_timer.stop()
                walk1_timer.stop()
                walkingLeft = False
                walkingRight = True
                walk1_timer.start()
            # Let go of walk right
            if walkingBoth == False and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                walkingRight = False
                walk2_timer.stop()
                walk1_timer.stop()
            # Let go of walk right while holding both
            elif walkingBoth == True and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                walk2_timer.stop()
                walk1_timer.stop()
                walkingRight = False
                walkingLeft = True
                walk1_timer.start()
        # Mouse Handler
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse Button 1
            if event.button == 1:
                # In Main Menu Screen
                # Play Button
                if startGame == False and settings == False and playButtonHover == True:
                    resetValues()
                    button.play()
                    intro.play()
                    startGame_timer.start()
                    playButtonHover = False
                    playButtonClicked = True
                    # Hide/Show Mouse
                    pygame.mouse.set_visible(False)
                if settings == False and settingsButtonHover == True:
                    button.play()
                    settingsMenu_timer.start()
                    settingsButtonHover = False
                    settingsButtonClicked = True
                # Exit Button
                if startGame == False and settings == False and exitButtonHover == True:
                    button.play()
                    exitGame()

                # In Death Screen
                # Restart Game
                if startGame == False and dead == True and restartButtonHover == True:
                    resetValues()
                    button.play()
                    stopSounds()
                    intro.play()
                    startGame_timer.start()
                    restartButtonHover = False
                    restartButtonClicked = True
                # Main Menu Button
                if startGame == False and dead == True and mainMenuButtonHover == True:
                    button.play()
                    stopSounds()
                    mainMenu_timer.start()
                    mainMenuButtonHover = False
                    mainMenuButtonClicked = True

                # In Pause Screen
                # Resume Button
                if pause == True and confirmationBox == False and settings == False and resumeButtonHover == True:
                    button.play()
                    resumeGame_timer.start()
                    resumeButtonHover = False
                    resumeButtonClicked = True
                    # Hide/Show Mouse
                    pygame.mouse.set_visible(False)
                # Settings Button
                if confirmationBox == False and settings == False and settingsButtonHover == True:
                    button.play()
                    settingsMenu_timer.start()
                    settingsButtonHover = False
                    settingsButtonClicked = True
                # Main Menu Button
                if pause == True and confirmationBox == False and settings == False and mainMenu2ButtonHover == True:
                    button.play()
                    confirmationBox_timer.start()
                    mainMenu2ButtonHover = False
                    mainMenu2ButtonClicked = True
                # In Confirmation Box
                if pause == True and confirmationBox == True:
                    # Yes Button
                    if confirmYesButtonHover == True:
                        button.play()
                        stopSounds()
                        mainMenu_timer.start()
                        confirmYesButtonHover = False
                        confirmYesButtonClicked = True
                    # No Button
                    if confirmNoButtonHover == True:
                        button.play()
                        confirmationBox = False
                # In Settings
                if settings == True:
                    # Done Button
                    if settingsDoneButtonHover == True:
                        button.play()
                        settingsDone_timer.start()
                        settingsDoneButtonHover = False
                        settingsDoneButtonClicked = True
                    # Master Down Button
                    if masterLeftButtonHover == True:
                        button.play()
                        masterVolumeDown()
                        volumeButtonReset_timer.start()
                        masterLeftButtonHover = False
                        masterLeftButtonClicked = True
                    # Master Up Button
                    if masterRightButtonHover == True:
                        button.play()
                        masterVolumeUp()
                        volumeButtonReset_timer.start()
                        masterRightButtonHover = False
                        masterRightButtonClicked = True
                    # Master Icon Button
                    if masterIconButtonHover == True:
                        button.play()
                        if masterVolumeMuted == False:
                            masterVolumeStored = masterVolume
                        masterVolumeMute(masterVolumeStored)
                        volumeButtonReset_timer.start()
                        masterIconButtonHover = False
                        masterIconButtonClicked = True
                    # Music Down Button
                    if musicLeftButtonHover == True:
                        button.play()
                        musicVolumeDown()
                        volumeButtonReset_timer.start()
                        musicLeftButtonHover = False
                        musicLeftButtonClicked = True
                    # Music Up Button
                    if musicRightButtonHover == True:
                        button.play()
                        musicVolumeUp()
                        volumeButtonReset_timer.start()
                        musicRightButtonHover = False
                        musicRightButtonClicked = True
                    # Music Icon Button
                    if musicIconButtonHover == True:
                        button.play()
                        if musicVolumeMuted == False:
                            musicVolumeStored = musicVolume
                        musicVolumeMute(musicVolumeStored)
                        volumeButtonReset_timer.start()
                        musicIconButtonHover = False
                        musicIconButtonClicked = True

                # Catalog Click to Buy
                if catalog == True:
                    # hover buy sniper button
                    if buyHoverP1_2 == True and ownSniperRifle == False:
                        if moneyCount >= 1000 and ownSniperRifle == False:
                            purchasedText = True
                            ownSniperRifle = True
                            hotbarSlot2 = False
                            moneyCount -= 1000
                            cashregister.play()
                        elif moneyCount < 1000 and ownSniperRifle == False:
                            insufFundsText = True
                            error.play()
                    # hover buy sawed off button
                    if buyHoverP1_3 == True and ownSawedOff == False:
                        if moneyCount >= 3000 and ownSawedOff == False:
                            purchasedText = True
                            ownSawedOff = True
                            hotbarSlot3 = False
                            moneyCount -= 3000
                            cashregister.play()
                        elif moneyCount < 3000 and ownSawedOff == False:
                            insufFundsText = True
                            error.play()
                    # hover buy ammo 1 button
                    if buyHoverP2_1 == True:
                        if moneyCount >= 50:
                            insufFundsText = False
                            purchasedText = True
                            revRoundsTotal += 24
                            moneyCount -= 50
                            cashregister.play()
                        elif moneyCount < 50:
                            purchasedText = False
                            insufFundsText = True
                            error.play()
                    # hover buy ammo 2 button
                    if buyHoverP2_2 == True:
                        if moneyCount >= 100:
                            insufFundsText = False
                            purchasedText = True
                            sniperRoundsTotal += 6
                            moneyCount -= 100
                            cashregister.play()
                        elif moneyCount < 100:
                            purchasedText = False
                            insufFundsText = True
                            error.play()
                    # hover buy ammo 3 button
                    if buyHoverP2_3 == True:
                        if moneyCount >= 100:
                            insufFundsText = False
                            purchasedText = True
                            buckRoundsTotal += 12
                            moneyCount -= 100
                            cashregister.play()
                        elif moneyCount < 100:
                            purchasedText = False
                            insufFundsText = True
                            error.play()
                    # hover buy hp beer button
                    if buyHoverP2_4 == True:
                        if moneyCount >= 100:
                            insufFundsText = False
                            purchasedText = True
                            hpPotionCount += 1
                            moneyCount -= 100
                            cashregister.play()
                        elif moneyCount < 100:
                            purchasedText = False
                            insufFundsText = True
                            error.play()

                if pause == False and dead == False and rolling == False:
                    # Revolver fires
                    if hotbarSlot1 == True:
                        if moveAbility == True and readyToFireRevolver == True:
                            if revRoundsMag > 0:
                                fire()
                                readyToFireRevolver = False
                                revolverFireDelay_timer.start()
                            else:
                                playerShoot = True
                                playerHolster = False
                                empty.stop()
                                empty.play()
                    # Sniper Rifle fires
                    if hotbarSlot2 == True and ownSniperRifle == True and scopeScreen == True:
                        if sniperRoundsMag > 0:
                            fire()
                        else:
                            empty.stop()
                            empty.play()
                    # Sawed-Off fires
                    if hotbarSlot3 == True and ownSawedOff == True:
                        if sawedOffRoundsMag > 0:
                            fire()
                        else:
                            playerShoot = True
                            playerHolster = False
                            empty.stop()
                            empty.play()
                    # Use HP Beer
                    if hotbarSlot6 == True and hpPotionCount > 0 and playerDrink == False and catalog == False:
                        hpPotion()
            # mouse scroll up
            if event.button == 4:
                if pause == False and dead == False:
                    prevSlot()
            if event.button == 5:
                if pause == False and dead == False:
                    nextSlot()

    # Mouse Position
    mouse_posx,mouse_posy = pygame.mouse.get_pos()
    # print(str(mouse_posx) + ", " + str(mouse_posy))

    # Death Buttons
    if dead == True:
        # Restart Button
        # Hover Button
        if (237 <= mouse_posx <= 363) and (313 <= mouse_posy <= 354) and restartButtonClicked == False:
            screen.blit(asset_restart_button_hover, (0, 0))
            restartButtonHover = True
        # Click Button
        elif (237 <= mouse_posx <= 363) and (313 <= mouse_posy <= 354) and restartButtonClicked == True:
            screen.blit(asset_restart_button_clicked, (0, 0))
            restartButtonHover = False
        # Normal Button
        else:
            screen.blit(asset_restart_button_normal, (0, 0))
            restartButtonHover = False

        # Main Menu Button
        # Hover Button
        if (238 <= mouse_posx <= 364) and (394 <= mouse_posy <= 438) and mainMenuButtonClicked == False:
            screen.blit(asset_main_menu_button_hover, (0, 0))
            mainMenuButtonHover = True
        # Click Button
        elif (238 <= mouse_posx <= 364) and (394 <= mouse_posy <= 438) and mainMenuButtonClicked == True:
            screen.blit(asset_main_menu_button_clicked, (0, 0))
            mainMenuButtonHover = False
        # Normal Button
        else:
            screen.blit(asset_main_menu_button_normal, (0, 0))
            mainMenuButtonHover = False

    # Main Menu -------------------------------------------------------------------------------------------------
    if startGame == False and dead == False:
        mainMenu()
    elif startGame == True:
        tumbleAuto = 15
        intromusic.stop()
    # Paused ----------------------------------------------------------------------------------------------------
    if pause == True:
        pauseGame()


    # Game Started ----------------------------------------------------------------------------------------------
    if startGame == True and pause == False:
        # sky
        screen.blit(asset_sky_day, (0, 0))
        # ground
        screen.blit(asset_ground_sand, (0, 403))
        # clouds
        screen.blit(asset_cloud1, (cloud1x-71, 37))
        screen.blit(asset_cloud2, (cloud2x-71, 121))
        # cactus
        screen.blit(asset_cactus, (cactusx, 209))
        screen.blit(asset_cactus, (cactusx+760, 209))
        # store
        screen.blit(asset_store, (store1x-97, 14))
        # saloon
        screen.blit(asset_saloon, (store2x-94, 13.5))
        # tumbleweed
        screen.blit(asset_tumbleweed, (tumweed1x-38, 330))


        # draw alive rattlesnakes
        for rattlesnake in Rattlesnake.instances:
            rattlesnake.work()
        # draw alive bandits
        for bandit in Bandit.instances:
            bandit.work()


        # shop interior
        if insideShop == True:
            screen.blit(asset_shop_interior, (store1x-250, 0))
        # shop interior
        if insideSaloon == True:
            screen.blit(asset_saloon_interior, (store2x-250, 0))


        # character model
        if standing == True:
            if lookingRight == True:
                # drink potion right
                if playerDrink == True:
                    screen.blit(asset_player_drink_right, (203, 246))
                else:
                    # base player right
                    screen.blit(asset_player_right, (217, 253))
                # idle legs
                if playerLegsIdle == True:
                    screen.blit(asset_player_legs_idle_right, (217, 252))
                # sniper rifle on back
                if ownSniperRifle == True and playerSniper == False:
                    screen.blit(asset_sniper_rifle_right, (237, 302))
                # revolver on hip
                if playerShoot == False:
                    screen.blit(asset_revolver_vert_right, (236, 344))
                # holster
                screen.blit(asset_holster_right, (217, 259))
                # hp beer in hand right
                if hotbarSlot6 == True and hpPotionCount > 0 and playerIdle == True:
                    screen.blit(asset_hearty_beer_right, (231, 353))
                # holding sniper right
                if playerSniper == True and playerWalk == False:
                    screen.blit(asset_sniper_right, (207, 349))
                # idle arms
                if playerIdle == True:
                    screen.blit(asset_player_arms_idle, (216, 253))
                # hand on holster
                if playerHolster == True and playerWalk == False:
                    screen.blit(asset_player_holster_right, (217, 253))
                # grab sniper
                if playerGrab == True:
                    screen.blit(asset_player_holster_right, (217, 253))
                # walk right
                if playerWalk == True:
                    # drink walk
                    if playerDrink == True:
                        screen.blit(asset_player_legs_walk_right, (217, 252))
                    # hold sniper walk
                    elif playerSniper == True:
                        screen.blit(asset_sniper_right, (225, 349))
                        screen.blit(asset_player_legs_walk_right, (217, 252))
                        screen.blit(asset_player_arms_walk_right, (217, 253))
                    # holster walk
                    elif playerHolster == True:
                        screen.blit(asset_player_legs_walk_right, (217, 252))
                        if playerShoot == False:
                            screen.blit(asset_revolver_vert_right, (236, 344))
                        screen.blit(asset_holster_right, (217, 259))
                        screen.blit(asset_player_holsterwalk_right, (217, 253))
                    else:
                        # hp beer in hand right
                        if hotbarSlot6 == True and hpPotionCount > 0:
                            screen.blit(asset_hearty_beer_right, (249, 352))
                        # default walk
                        screen.blit(asset_player_arms_walk_right, (217, 253))
                        if ownSniperRifle == True and playerSniper == False:
                            screen.blit(asset_sniper_rifle_right, (237, 302))
                        screen.blit(asset_player_legs_walk_right, (217, 252))
                        if playerShoot == False:
                            screen.blit(asset_revolver_vert_right, (236, 344))
                        screen.blit(asset_holster_right, (217, 259))
                # bandana right
                if playerDrink == False:
                    screen.blit(asset_bandana_right, (217, 253))
                # shoot revolver right
                if playerShoot == True and hotbarSlot1 == True:
                    screen.blit(asset_revolver_right, (279, 311))
                    screen.blit(asset_player_shoot_right, (227, 252))
                    screen.blit(asset_muzzleflash_right, (bulletx-12, 307))
                # shoot sawed off right
                if playerShoot == True and hotbarSlot3 == True:
                    screen.blit(asset_revolver_vert_right, (236, 344))
                    screen.blit(asset_holster_right, (217, 259))
                    if sawedOffRoundsMag >= 1:
                        screen.blit(asset_sawed_off_half_right, (276, 305))
                    elif sawedOffRoundsMag == 0:
                        screen.blit(asset_sawed_off_right, (276, 305))
                    screen.blit(asset_player_shoot_right, (227, 252))
                    screen.blit(asset_muzzleflash_buck_right, (bulletx-2, 295))
            if lookingLeft == True:
                # revolver on hip
                if playerShoot == False:
                    screen.blit(asset_revolver_vert_grip_left, (248, 342))
                # holding sniper left
                if playerSniper == True and playerWalk == False:
                    screen.blit(asset_sniper_left, (190, 349))
                # hp beer in hand right
                if hotbarSlot6 == True and hpPotionCount > 0 and playerIdle == True:
                    screen.blit(asset_hearty_beer_left, (240, 353))
                # drink potion left
                if playerDrink == True:
                    screen.blit(asset_player_drink_left, (198, 245))
                else:
                    # base player left
                    screen.blit(asset_player_left, (217, 253))
                # idle legs
                if playerLegsIdle == True:
                    screen.blit(asset_player_legs_idle_left, (217, 252))
                # idle arms
                if playerIdle == True:
                    screen.blit(asset_player_arms_idle, (217, 253))
                # hand on holster
                if playerHolster == True and playerWalk == False:
                    screen.blit(asset_player_holster_left, (217, 253))
                # grab sniper
                if playerGrab == True:
                    screen.blit(asset_player_holster_left, (217, 253))
                # sniper rifle on back
                if ownSniperRifle == True and playerSniper == False:
                    screen.blit(asset_sniper_rifle_left, (253, 302))
                    # walk left
                if playerWalk == True:
                    # drink walk
                    if playerDrink == True:
                        screen.blit(asset_player_legs_walk_left, (217, 252))
                    # hold sniper walk
                    elif playerSniper == True:
                        screen.blit(asset_sniper_left, (207, 348))
                        screen.blit(asset_player_left, (217, 253))
                        screen.blit(asset_player_arms_walk_left, (217, 253))
                        screen.blit(asset_player_legs_walk_left, (217, 252))
                    # holster walk
                    elif playerHolster == True:
                        screen.blit(asset_player_holsterwalk_left, (217, 253))
                        if ownSniperRifle == True and playerSniper == False:
                            screen.blit(asset_sniper_rifle_left, (253, 302))
                        screen.blit(asset_player_legs_walk_left, (217, 252))
                    else:
                        # hp beer in hand left
                        if hotbarSlot6 == True and hpPotionCount > 0:
                            screen.blit(asset_hearty_beer_left, (262, 352))
                        # default walk
                        screen.blit(asset_player_arms_walk_left, (217, 253))
                        if ownSniperRifle == True and playerSniper == False:
                            screen.blit(asset_sniper_rifle_left, (253, 302))
                        screen.blit(asset_player_legs_walk_left, (217, 252))
                # shoot revolver left
                if playerShoot == True and hotbarSlot1 == True:
                    screen.blit(asset_player_shoot_left, (207, 252))
                    screen.blit(asset_player_left, (217, 253))
                    screen.blit(asset_player_arms_idle, (217, 253))
                    screen.blit(asset_revolver_left, (182, 311))
                    screen.blit(asset_muzzleflash_left, (bulletx-250, 307))
                # shoot sawed off left
                if playerShoot == True and hotbarSlot3 == True:
                    screen.blit(asset_player_shoot_left, (207, 252))
                    screen.blit(asset_player_left, (217, 253))
                    screen.blit(asset_player_arms_idle, (217, 253))
                    if sawedOffRoundsMag >= 1:
                        screen.blit(asset_sawed_off_half_left, (172, 305))
                    elif sawedOffRoundsMag == 0:
                        screen.blit(asset_sawed_off_left, (172, 305))
                    screen.blit(asset_muzzleflash_buck_left, (bulletx-249, 295))
                # bandana left
                screen.blit(asset_bandana_left, (217, 253))
        # Roll
        if rolling == True:
            if lookingRight == True:
                if playerRoll1Right == True:
                    screen.blit(asset_player_roll1_right, (150, 265))
                if playerRoll2Right == True:
                    screen.blit(asset_player_roll2_right, (150, 265))
                if playerRoll3Right == True:
                    screen.blit(asset_player_roll3_right, (150, 265))
            if lookingLeft == True:
                if playerRoll1Left == True:
                    screen.blit(asset_player_roll1_left, (150, 265))
                if playerRoll2Left == True:
                    screen.blit(asset_player_roll2_left, (150, 265))
                if playerRoll3Left == True:
                    screen.blit(asset_player_roll3_left, (150, 265))
        # Cooldown sweat
        if standing == True and rollReady == False:
            if lookingRight:
                screen.blit(asset_player_cooldown_sweat_right, (212, cooldown_sweat_y))
            if lookingLeft:
                screen.blit(asset_player_cooldown_sweat_left, (222, cooldown_sweat_y))
        # HP Gain Particles
        if standing == True and healing == True:
            screen.blit(asset_player_hp_gain_particle, (208, hp_gain1_y))
            screen.blit(asset_player_hp_gain_particle, (240, hp_gain2_y))
            screen.blit(asset_player_hp_gain_particle, (282, hp_gain3_y))

        # Loot
        if looting == True:
            if lookingRight == True:
                screen.blit(asset_player_loot_right, (180, 255))
            if lookingLeft == True:
                screen.blit(asset_player_loot_left, (173, 255))


        # draw dead rattlesnakes
        for rattlesnake in Rattlesnake.instances:
            rattlesnake.draw_dead()

        # draw dead bandits
        for bandit in Bandit.instances:
            bandit.draw_dead()



        # catalog pages
        if insideShop == True:
            if catalog == True:
                if catalogPage1 == True:
                    screen.blit(asset_catalog_1, (0, 0))
                elif catalogPage2 == True:
                    screen.blit(asset_catalog_2, (0, 0))
                elif catalogPage3 == True:
                    screen.blit(asset_catalog_3, (0, 0))

        # catalog weapon prices
        if catalogPage2 == True:
            screen.blit(asset_text_owned, (220, 203))
            if ownSniperRifle == True:
                screen.blit(asset_text_owned, (220, 294))
            if ownSniperRifle == False:
                if moneyCount < 1000:
                    screen.blit(asset_text_1000_red, (226, 293))
                elif moneyCount >= 1000:
                    screen.blit(asset_text_1000_green, (226, 293))
            if ownSawedOff == True:
                screen.blit(asset_text_owned, (220, 384))
            if ownSawedOff == False:
                if moneyCount < 3000:
                    screen.blit(asset_text_3000_red, (226, 383))
                elif moneyCount >= 3000:
                    screen.blit(asset_text_3000_green, (226, 383))
        if catalogPage3 == True:
            if moneyCount < 100:
                # hearty beer
                screen.blit(asset_text_100_red, (505, 202))
                # 30-50 rounds
                screen.blit(asset_text_100_red, (235, 293))
                # 12 gauge rounds
                screen.blit(asset_text_100_red, (235, 383))
            elif moneyCount >= 100:
                # hearty beer
                screen.blit(asset_text_100_green, (505, 202))
                # 30-50 rounds
                screen.blit(asset_text_100_green, (235, 293))
                # 12 gauge rounds
                screen.blit(asset_text_100_green, (235, 383))
            if moneyCount < 50:
                # .45 rounds
                screen.blit(asset_text_50_red, (240, 200))
            elif moneyCount >= 50:
                # .45 rounds
                screen.blit(asset_text_50_green, (240, 200))

        # Catalog Buy Hover
        if catalogPage2 == True:
            # revolver buy hover
            if (186 <= mouse_posx <= 214) and (127 <= mouse_posy <= 138):
                buyHoverP1_1 = False  # revolver is already owned, no hover
            # sniper buy hover
            if (209 <= mouse_posx <= 236) and (227 <= mouse_posy <= 238):
                buyHoverP1_2 = True
                screen.blit(asset_buy_hover_p1_2, (0, 0))
            else:
                buyHoverP1_2 = False
            # sawedoff buy hover
            if (180 <= mouse_posx <= 207) and (316 <= mouse_posy <= 327):
                buyHoverP1_3 = True
                screen.blit(asset_buy_hover_p1_3, (0, 0))
            else:
                buyHoverP1_3 = False
        if catalogPage3 == True:
            # ammo1 buy hover
            if (197 <= mouse_posx <= 224) and (128 <= mouse_posy <= 139):
                buyHoverP2_1 = True
                screen.blit(asset_buy_hover_p2_1, (0, 0))
            else:
                buyHoverP2_1 = False
            # ammo2 buy hover
            if (218 <= mouse_posx <= 245) and (225 <= mouse_posy <= 236):
                buyHoverP2_2 = True
                screen.blit(asset_buy_hover_p2_2, (0, 0))
            else:
                buyHoverP2_2 = False
            # ammo3 buy hover
            if (207 <= mouse_posx <= 234) and (318 <= mouse_posy <= 329):
                buyHoverP2_3 = True
                screen.blit(asset_buy_hover_p2_3, (0, 0))
            else:
                buyHoverP2_3 = False
            # HP beer buy hover
            if (500 <= mouse_posx <= 527) and (128 <= mouse_posy <= 139):
                buyHoverP2_4 = True
                screen.blit(asset_buy_hover_p2_4, (0, 0))
            else:
                buyHoverP2_4 = False


        # sniper scope
        if ownSniperRifle == True:
            if scopeScreen == True:
                scoped()
            else:
                breath.stop()
                heartbeat.stop()



        # Constant Refresh -------------------------------------------------------------------------------------

        # HUD
        if startGame == True and scopeScreen == False:
            showHUD()

        # Player Model Refresh
        playerLegsIdle = True
        playerWalk = False

        # Interact text change
        if hotbarSlot2 == False:
            if demoMode == True:
                interact_text = font1.render("ACTION (W)", True, (150, 240, 41))
            else:
                interact_text = font1.render("INTERACT", True, (255, 255, 255))
        elif hotbarSlot2 == True:
            if demoMode == True:
                interact_text = font1.render("SCOPE (W)", True, (150, 240, 41))
            else:
                interact_text = font1.render("SCOPE", True, (255, 255, 255))


        playerGrab = False
        if playerHolster == False and playerShoot == False and playerDrink == False:
            playerIdle = True
        if (playerHolster == True or playerSniper == True) and insideShop == True:
            screen.blit(shopWarning_text, (store1x + 527, 207))

        # If trying to walk both left and right
        if walkingLeft and walkingRight:
            walkingBoth = True
        else:
            walkingBoth = False

        # Check if dead
        if playerHP <= 0:
            playerDead()

        # If wave is completed, start a new one
        if Bandit.alive == 0:
            startWave_timer.start()

        # check for interact
        interactCheck()

        # check for highscore
        if score > highscore and (devMode == False or demoMode == True):
            highscore = score

        # check for out of ammo or needed reload
        # revolver --------------------
        if revRoundsMag <= 0 and revRoundsTotal > 0:
            revolverOutMag = True
        else:
            revolverOutMag = False

        if revRoundsTotal <= 0 and revRoundsMag <= 0:
            revolverOutAmmo = True
            revolverOutMag = False
        else:
            revolverOutAmmo = False
        # sniper rifle ----------------
        if sniperRoundsMag <= 0 and sniperRoundsTotal > 0:
            sniperOutMag = True
        else:
            sniperOutMag = False

        if sniperRoundsTotal <= 0 and sniperRoundsMag <= 0:
            sniperOutAmmo = True
            sniperOutMag = False
        else:
            sniperOutAmmo = False
        # sawed off ----------------
        if sawedOffRoundsMag <= 0 and buckRoundsTotal > 0:
            sawedOffOutMag = True
        else:
            sawedOffOutMag = False

        if buckRoundsTotal <= 0 and sawedOffRoundsMag <= 0:
            sawedOffOutAmmo = True
            sawedOffOutMag = False
        else:
            sawedOffOutAmmo = False

        # check for whether or not to show reload
        # revolver
        if revolverOutMag and hotbarSlot1:
            reloadUI = True
        # sniper
        elif sniperOutMag and hotbarSlot2:
            reloadUI = True
            interactText = False
        # sawed off
        elif sawedOffOutMag and hotbarSlot3:
            reloadUI = True
            interactText = False
        else:
            reloadUI = False
        # check for whether or not to show out of ammo
        # revolver
        if revolverOutAmmo and hotbarSlot1:
            reloadUI = False
            outAmmoUI = True
        # sniper
        elif sniperOutAmmo and hotbarSlot2:
            reloadUI = False
            outAmmoUI = True
            interactText = False
        # sawed off
        elif sawedOffOutAmmo and hotbarSlot3:
            reloadUI = False
            outAmmoUI = True
            interactText = False
        else:
            outAmmoUI = False

        # disable interact text while looting
        if looting == True:
            interactText = False


        # text refresh
        playerHP_text = font2.render((str(playerHP)), True, (255, 255, 255))
        playerScore_text = font2.render((str(score)), True, (255, 255, 255))
        playerMoney_text = font2.render((str(moneyCount)), True, (255, 255, 255))
        revolverAmmo_text = font2.render((str(revRoundsMag) + "/" + str(revRoundsTotal)), True, (255, 255, 255))
        sniperAmmo_text = font2.render((str(sniperRoundsMag) + "/" + str(sniperRoundsTotal)), True, (255, 255, 255))
        sawedOffAmmo_text = font2.render((str(sawedOffRoundsMag) + "/" + str(buckRoundsTotal)), True, (255, 255, 255))
        potionCount_text = font1.render((str(hpPotionCount)), True, (255, 255, 255))
        deathScore_text = font1.render(("Score: " + str(score)), True, (255, 255, 255))
        masterVolume_text = font1.render((str(masterVolume)), True, (255, 255, 255))
        musicVolume_text = font1.render((str(musicVolume)), True, (255, 255, 255))
        playerHighscore_text = font1.render("Highscore: " + (str(highscore)), True, (255, 255, 255))
        wave_text = font5.render("Wave " + str(wave), True, (240, 177, 29))
        wave_text_rect = wave_text.get_rect(center=[300, 150])
        infinity_text = font2.render("-1", True, (255, 255, 255))

        # volume refresh
        step.set_volume(masterVolume)
        woodstep.set_volume(masterVolume)
        button.set_volume(masterVolume)
        griprevolver.set_volume(masterVolume)
        shot.set_volume(masterVolume)
        empty.set_volume(masterVolume)
        reload.set_volume(masterVolume)
        revolverspin.set_volume(masterVolume)
        death.set_volume(masterVolume)
        playerhit.set_volume(masterVolume)
        banpain.set_volume(masterVolume)
        snipershot.set_volume(masterVolume)
        heartbeat.set_volume(masterVolume)
        breath.set_volume(masterVolume)
        door.set_volume(masterVolume)
        openbook.set_volume(masterVolume)
        turnpage.set_volume(masterVolume)
        cashregister.set_volume(masterVolume)
        error.set_volume(masterVolume)
        potion.set_volume(masterVolume)
        sniper_reload.set_volume(masterVolume)
        combatroll.set_volume(masterVolume)
        lootBody.set_volume(masterVolume)
        sawedoffshot.set_volume(masterVolume)
        sawedoffopen.set_volume(masterVolume)
        loadshell.set_volume(masterVolume)
        burp.set_volume(masterVolume)
        burp2.set_volume(masterVolume)
        burp3.set_volume(masterVolume)
        saloon_ambience.set_volume(masterVolume)
        outside_ambience.set_volume(masterVolume)
        venom_heartbeat.set_volume(masterVolume)
        rattlesnake_rattle.set_volume(masterVolume)
        rattlesnake_strike.set_volume(masterVolume)
        intromusic.set_volume(musicVolume * masterVolume)
        intro.set_volume(musicVolume * masterVolume)
        music.set_volume(musicVolume * masterVolume)
        train_distant.set_volume(masterVolume)

        # building loop
        if insideShop == False and insideSaloon == False:
            if store2x <= -500:
                store1x += 1900
                store2x += 1900
            elif store2x >= 1400:
                store1x -= 1900
                store2x -= 1900
                cactusx -= 1900
            if cactusx <= -1000:
                cactusx += 1900
            elif cactusx >= 900:
                cactusx -= 1900

        # active hotbar slot position
        if hotbarSlot1 == True:
            activeSlotx1 = 150
            activeSlotx2 = 200
        elif hotbarSlot2 == True:
            activeSlotx1 = 200
            activeSlotx2 = 250
        elif hotbarSlot3 == True:
            activeSlotx1 = 250
            activeSlotx2 = 300
        elif hotbarSlot4 == True:
            activeSlotx1 = 300
            activeSlotx2 = 350
        elif hotbarSlot5 == True:
            activeSlotx1 = 350
            activeSlotx2 = 400
        elif hotbarSlot6 == True:
            activeSlotx1 = 400
            activeSlotx2 = 450
        else:
            activeSlotx1 = -500
            activeSlotx2 = -500

        # bandit fp
        for bandit in Bandit.instances:
            # refresh values
            if bandit.hp > 0:
                # calculate distance between bandit and player
                bandit_distance = abs(bandit.x_location - 260)
                if bandit_distance == 0:
                    bandit_distance = 1
                # if statement fixes negative bug
                if bandit_distance < 500:
                    # scopeWalk gets larger as bandit_distance gets smaller
                    scopeWalk = 500 - bandit_distance


        # cloud pos
        cloud1x -= cloudAuto
        if cloud1x + 85 <= -100:
            cloud1x = 800
        cloud2x -= cloudAuto
        if cloud2x + 85 <= -100:
            cloud2x = 1100

        # tumweed pos
        tumweed1x -= tumbleAuto
        if tumweed1x <= tumweedReset:
            tumweed1x = tumweedSpawn

        # bullet reset
        bulletx = -330


        # cooldown sweat pos
        if rollReady == False:
            cooldown_sweat_y += 1
        if cooldown_sweat_y > 273:
            cooldown_sweat_y = 252

        # hp gain particle1 pos
        if healing == True:
            hp_gain1_y -= 1
        if hp_gain1_y < random.randrange(226,232):
            hp_gain1_y = random.randrange(247,262)
        # hp gain particle2 pos
        if healing == True:
            hp_gain2_y -= 1
        if hp_gain2_y < random.randrange(214,220):
            hp_gain2_y = random.randrange(230,240)
        # hp gain particle3 pos
        if healing == True:
            hp_gain3_y -= 1
        if hp_gain3_y < random.randrange(227,236):
            hp_gain3_y = random.randrange(247,260)

        if banMoveAbility == True:
            banMove = 8
        elif banMoveAbility == False:
            banMove = 0
    pygame.display.update()
    clock.tick(25)

# End
