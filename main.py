## JOURNEY'S WILD WEST
## v0.4
## Developed by: Josh Collins
## ---------------------------

# Modules
import pygame
import random
import time
import sys

try:
    import simplegui

except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# window resolution
height = 600
width = 600

# pygame initialization
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
clock = pygame.time.Clock()

# window properties
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("JOURNEYS: WILD WEST")
pygame.display.set_icon(pygame.image.load("assets/icon/window_icon.png"))
collapse = True
version = "0.4"

# values and statements
if collapse:
    # MAKE SURE TO ALSO CHANGE VALUES IN RESETVALUES METHOD -------------------------------------------------------
    # player vals
    playerHP = 100
    bodyWeight = 12
    moneyCount = 0
    revRoundsMag = 6
    revRoundsTotal = 24
    revolverFireRate = 12
    revolverReloadSpeed = 450
    sniperRoundsMag = 1
    sniperRoundsTotal = 3
    hpPotionCount = 5
    drinkTime = 100
    score = 0

    # speed
    speedMove = 50
    boardWalk = 80
    cloudMove = 8
    cloudAuto = 0.2
    tumbleAuto = 15
    banMove = 8

    # x-pos
    cloud1x = 100
    cloud2x = 600
    tumweed1x = 700
    store1x = 700
    store2x = 1400
    cactusx = 450

    activeSlotx1 = -50
    activeSlotx2 = -50
    bulletx = 330

    # ban 1
    banHP = 100
    banx1 = 1990
    banFPx1 = 300
    scopeWalk = 0
    # ban 2
    ban2HP = 100
    banx2 = 2490
    ban2FPx1 = 300
    scope2Walk = 0
    # ban 3
    ban3HP = 100
    banx3 = -1000
    ban3FPx1 = 300
    scope3Walk = 0

    # statements
    moveAbility = True
    banMoveAbility = True
    interactText = False
    buyText = False
    sitting = False
    standing = True
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
    dead = False
    scopeScreen = False
    ban1left = False
    ban2left = False
    ban3left = True
    ban1InScope = False
    ban2InScope = False
    ban3InScope = False
    insideShop = False
    ownSniperRifle = True
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
    # MAKE SURE TO ALSO CHANGE VALUES IN RESETVALUES METHOD -------------------------------------------------------


# audio
if collapse:
    masterVolume = 1  # (0-1)
    musicVolume = 1  # (0-1)
    step = pygame.mixer.Sound('sounds/step.wav')
    woodstep = pygame.mixer.Sound('sounds/woodstep.wav')
    intro = pygame.mixer.Sound('sounds/start_music.wav')
    button = pygame.mixer.Sound('sounds/button.wav')
    griprevolver = pygame.mixer.Sound('sounds/griprevolver.wav')
    shot = pygame.mixer.Sound('sounds/shot.wav')
    empty = pygame.mixer.Sound('sounds/empty.wav')
    reload = pygame.mixer.Sound('sounds/reload.wav')
    death = pygame.mixer.Sound('sounds/death.wav')
    playerhit = pygame.mixer.Sound('sounds/playerhit.wav')
    banpain = pygame.mixer.Sound('sounds/banpain.wav')
    snipershot = pygame.mixer.Sound('sounds/snipershot.wav')
    heartbeat = pygame.mixer.Sound('sounds/heartbeat.wav')
    breath = pygame.mixer.Sound('sounds/breath.wav')
    intromusic = pygame.mixer.Sound('sounds/menu_music.wav')
    door = pygame.mixer.Sound('sounds/door.wav')
    openbook = pygame.mixer.Sound('sounds/openbook.wav')
    turnpage = pygame.mixer.Sound('sounds/turnpage.wav')
    cashregister = pygame.mixer.Sound('sounds/cashregister.wav')
    error = pygame.mixer.Sound('sounds/error.wav')
    music = pygame.mixer.Sound('sounds/bg_music.wav')
    potion = pygame.mixer.Sound('sounds/beer_drink.wav')
    sniper_reload = pygame.mixer.Sound('sounds/sniper_reload.wav')


# assets
if collapse:
    asset_cactus = pygame.image.load("assets/vegetation/cactus.png")
    asset_cloud1 = pygame.image.load("assets/sky/cloud1.png")
    asset_cloud2 = pygame.image.load("assets/sky/cloud2.png")
    asset_saloon = pygame.image.load("assets/buildings/cianfarano_saloon.png")
    asset_store = pygame.image.load("assets/buildings/solee_os_store.png")
    asset_hotbar = pygame.image.load("assets/UI/hotbar.png")
    asset_revolver = pygame.image.load("assets/UI/revolver_icon.png")
    asset_sniper = pygame.image.load("assets/UI/sniper_rifle_icon.png")
    asset_bandit1 = pygame.image.load("assets/npc/bandit1.png")
    asset_bandit2 = pygame.image.load("assets/npc/bandit2.png")
    asset_bandit3 = pygame.image.load("assets/npc/bandit3.png")
    asset_bandit1right = pygame.image.load("assets/npc/bandit1right.png")
    asset_bandit2right = pygame.image.load("assets/npc/bandit2right.png")
    asset_bandit3right = pygame.image.load("assets/npc/bandit3right.png")
    asset_bandit1_dead = pygame.image.load("assets/npc/bandit1dead.png")
    asset_bandit2_dead = pygame.image.load("assets/npc/bandit2dead.png")
    asset_bandit3_dead = pygame.image.load("assets/npc/bandit3dead.png")
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
    asset_muzzleflash_right = pygame.image.load("assets/weapons/muzzle_flash_bullet_right.png")
    asset_muzzleflash_left = pygame.image.load("assets/weapons/muzzle_flash_bullet_left.png")
    asset_sniperscope = pygame.image.load("assets/weapons/sniper_scope.png")
    asset_bandit1_fp = pygame.image.load("assets/npc/bandit1_fp.png")
    asset_bandit2_fp = pygame.image.load("assets/npc/bandit2_fp.png")
    asset_bandit3_fp = pygame.image.load("assets/npc/bandit3_fp.png")
    asset_scope_back_right = pygame.image.load("assets/weapons/scope_back_right.png")
    asset_scope_back_left = pygame.image.load("assets/weapons/scope_back_left.png")
    asset_sniper_rifle_right = pygame.image.load("assets/weapons/sniper_rifle_right.png")
    asset_sniper_rifle_left = pygame.image.load("assets/weapons/sniper_rifle_left.png")
    asset_shop_interior = pygame.image.load("assets/buildings/shop_interior.png")
    asset_text_1000_green = pygame.image.load("assets/UI/text_1000_green.png")
    asset_text_1000_red = pygame.image.load("assets/UI/text_1000_red.png")
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

# text
if collapse:
    font1 = pygame.font.SysFont("Times New Roman", 13, False)
    font2 = pygame.font.SysFont("Times New Roman", 18, False)
    font3 = pygame.font.SysFont("ebrima", 20, True)
    # syntax - (Name, Size, Bold, Italic)

    ban1Tag = font1.render("Bandit: Nicholas", True, (150,240,41))
    ban1HPTag = font1.render(("HP: " + str(banHP)), True, (255,255,255))
    ban2Tag = font1.render("Bandit: Darius", True, (150,240,41))
    ban2HPTag = font1.render(("HP: " + str(ban2HP)), True, (255,255,255))
    ban3Tag = font1.render("Bandit: Olyander", True, (150,240,41))
    ban3HPTag = font1.render(("HP: " + str(ban3HP)), True, (255,255,255))
    playerHP_text = font2.render((str(playerHP)), True, (255,255,255))
    playerScore_text = font2.render((str(score)), True, (255,255,255))
    playerMoney_text = font2.render((str(moneyCount)), True, (255,255,255))
    revolverAmmo_text = font2.render((str(revRoundsMag) + "/" + str(revRoundsTotal)), True, (255,255,255))
    sniperAmmo_text = font2.render((str(sniperRoundsMag) + "/" + str(sniperRoundsTotal)), True, (255,255,255))
    blankAmmo_text = font2.render("-/-", True, (255,255,255))
    reloadFront_text = font1.render("RELOAD (R)", True, (255,0,0))
    reloadBack_text = font1.render("RELOAD (R)", True, (0,0,0))
    outAmmoFront_text = font1.render("Out of Ammo", True, (255,0,0))
    outAmmoBack_text = font1.render("Out of Ammo", True, (0,0,0))
    interact_text = font1.render("INTERACT", True, (255,255,255))
    buy_text = font1.render("BUY", True, (255,255,255))
    potionCount_text = font1.render((str(hpPotionCount)), True, (255,255,255))
    clickPlay_text = font1.render("Click Here to PLAY", True, (255,255,255))
    deathScore_text = font2.render(("Score: " + str(score)), True, (255,255,255))
    shopWarning_text = font1.render("\"Take your hand off the gun, son..\"", True, (0, 0, 0))
    version_text = font1.render(("v " + version), True, (255, 255, 255))
    masterVolume_text = font1.render((str(masterVolume)), True, (255, 255, 255))
    musicVolume_text = font1.render((str(musicVolume)), True, (255, 255, 255))
    # syntax - (Message, AntiAliasing, Color, Background=None)


def worldLeft():
    global height, width, cloud1x, cloud2x, speedMove, cloudMove, cloudAuto, interactText, moveAbility, sitting,\
        standing, bodyWeight, moneyCount, showMoney, moneyPickText, purchasedText, insufFundsText, buyText,\
        cactusx, store1x, store2x, tumweed1x, startGame, banx1, banHP, banx2, ban2HP, ban3HP, banx3, ban3FPx1, \
        scope3Walk, playerIdle, playerWalk, playerLegsIdle, playerShoot, playerHolster, playerSniper

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

    cloud1x += cloudMove
    if cloud1x + 85 >= 800:
        cloud1x = -100
    cloud2x += cloudMove
    if cloud2x + 85 >= 800:
        cloud2x = -100
    cactusx += speedMove
    store1x += speedMove
    store2x += speedMove
    tumweed1x += speedMove
    banx1 += speedMove
    banx2 += speedMove
    banx3 += speedMove


def worldRight():
    global height, width, cloud1x, cloud2x, speedMove, cloudMove, cloudAuto, interactText, moveAbility, sitting,\
        standing, bodyWeight, moneyCount, showMoney, moneyPickText, purchasedText,insufFundsText,\
        buyText, cactusx, store1x, store2x, tumweed1x, startGame, banx1, banHP, banx2, ban2HP,ban3HP, banx3, \
        ban3FPx1,scope3Walk, playerIdle, playerWalk, playerLegsIdle, playerShoot,playerHolster, playerSniper

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

    cloud1x -= cloudMove
    if cloud1x + 85 <= -100:
        cloud1x = 800
    cloud2x -= cloudMove
    if cloud2x + 85 <= -100:
        cloud2x = 1100
    cactusx -= speedMove
    store1x -= speedMove
    store2x -= speedMove
    tumweed1x -= speedMove
    banx1 -= speedMove
    banx2 -= speedMove
    banx3 -= speedMove


def walkRight():
    global moveAbility, hotbarSlot2, moneyPickText, interactText, insufFundsText, purchasedText, lookingRight,\
        lookingLeft, hotbarSlot1, store1x, store2x, scopeScreen, insideShop, playerShoot, playerHolster, playerSniper

    if moveAbility == True and pause == False:
        if scopeScreen == False:
            worldRight()
            disableText()
            lookingRight = True
            lookingLeft = False
            if hotbarSlot1 == True:
                playerHolster = True
            if insideShop == False:
                step.stop()
                step.play()
            elif insideShop == True:
                woodstep.stop()
                woodstep.play()
    if store1x <= 100 and store1x >= 0:
        if playerHolster == False and playerShoot == False and scopeScreen == False and insideShop == False:
            interactText = True


def walkLeft():
    global moveAbility, hotbarSlot2, moneyPickText, interactText, insufFundsText, purchasedText, lookingRight,\
        lookingLeft, hotbarSlot1, store1x, store2x, scopeScreen, insideShop, playerShoot, playerHolster

    if moveAbility == True and pause == False:
        if scopeScreen == False:
            worldLeft()
            disableText()
            lookingRight = False
            lookingLeft = True
            if hotbarSlot1 == True:
                playerHolster = True
            if insideShop == False:
                step.stop()
                step.play()
            elif insideShop == True:
                woodstep.stop()
                woodstep.play()
    if store1x <= 100 and store1x >= 0:
        if playerHolster == False and playerShoot == False and scopeScreen == False and insideShop == False:
            interactText = True


def disableText():
    global moneyPickText, interactText, insufFundsText, purchasedText
    moneyPickText = False
    insufFundsText = False
    purchasedText = False
    if playerSniper == False:
        interactText = False


def fire():
    global score, moneyCount, startGame, moveAbility, hotbarSlot2, hotbarSlot6, dead, bulletx, hotbarSlot1, \
        lookingLeft, lookingRight, revRoundsMag, reloadUI, outAmmoUI, interactText, banHP, banx2, ban2HP, scopeScreen,\
        ban3HP, banx3, ban3FPx1, scope3Walk, playerShoot, playerHolster, revRoundsTotal,sniperRoundsMag,\
        sniperRoundsTotal, playerSniper

    # Revolver
    if hotbarSlot1 == True:
        playerShoot = True
        playerHolster = False
        interactText = False
        if revRoundsMag > 0:
            if lookingRight == True:
                bulletx = 330
            if lookingLeft == True:
                bulletx = 330
            shot.stop()
            shot.play()
            revRoundsMag -= 1
            revolver_reload_timer.stop()
            reload.stop()

        elif revRoundsMag == 0:
            empty.stop()
            empty.play()
            reloadUI = True

        if revRoundsMag > 0:
            if lookingRight:
                if banx1 <= 600 and banx1 >= 250:
                    if banHP > -10:
                        banHP -= 20
                        if banHP == 0:
                            banpain.play()
                            score += 1
                            giveMoney()
                if banx2 <= 600 and banx2 >= 250:
                    if ban2HP > -10:
                        ban2HP -= 20
                        if ban2HP == 0:
                            banpain.play()
                            score += 1
                            giveMoney()
                if banx3 <= 600 and banx3 >= 250:
                    if ban3HP > -10:
                        ban3HP -= 20
                        if ban3HP == 0:
                            banpain.play()
                            score += 1
                            giveMoney()
            if lookingLeft:
                if banx1 >= 0 and banx1 <= 250:
                    if banHP > -10:
                        banHP -= 20
                        if banHP == 0:
                            banpain.play()
                            score += 1
                            giveMoney()
                if banx2 >= 0 and banx2 <= 250:
                    if ban2HP > -10:
                        ban2HP -= 20
                        if ban2HP == 0:
                            banpain.play()
                            score += 1
                            giveMoney()
                if banx3 >= 0 and banx3 <= 250:
                    if ban3HP > -10:
                        ban3HP -= 20
                        if ban3HP == 0:
                            banpain.play()
                            score += 1
                            giveMoney()

    # sniper rifle
    if hotbarSlot2 == True and scopeScreen == True:
        interactText = False
        if sniperRoundsMag > 0:
            snipershot.stop()
            snipershot.play()
            scopeScreen = False
            sniperRoundsMag -= 1
            sniper_reload.stop()
        else:
            empty.stop()
            empty.play()
        if lookingRight:
            if banx1 <= 600 and banx1 >= 250:
                if banHP > -10:
                    banHP -= 100
                    if banHP == 0:
                        banpain.play()
                        score += 1
                        giveMoney()
            if banx2 <= 600 and banx2 >= 250:
                if ban2HP > -10:
                    ban2HP -= 100
                    if ban2HP == 0:
                        banpain.play()
                        score += 1
            if banx3 <= 600 and banx3 >= 250:
                if ban3HP > -10:
                    ban3HP -= 100
                    if ban3HP == 0:
                        banpain.play()
                        score += 1
                        giveMoney()
        if lookingLeft:
            if banx1 >= 0 and banx1 <= 250:
                if banHP > -10:
                    banHP -= 100
                    if banHP == 0:
                        banpain.play()
                        score += 1
                        giveMoney()
            if banx2 >= 0 and banx2 <= 250:
                if ban2HP > -10:
                    ban2HP -= 100
                    if ban2HP == 0:
                        banpain.play()
                        score += 1
                        giveMoney()
            if banx3 >= 0 and banx3 <= 250:
                if ban3HP > -10:
                    ban3HP -= 100
                    if ban3HP == 0:
                        banpain.play()
                        score += 1
                        giveMoney()


def hpPotion():
    global playerHP, hpPotionCount, playerDrink
    for i in range(0, 1):
        time.sleep(0.09)
        for j in range(0, 50):
            if playerHP < 100:
                playerHP += 1
            else:
                j = 50
    hpPotionCount -= 1
    playerDrink = True
    potion.stop()
    potion.play()


def getBanditRespawn():
    x = random.randint(-1200, 1200)
    if x <= 700 and x >= -100:
        x += 900
    return x


def giveMoney():
    global moneyCount
    x = random.randint(30, 100)
    moneyCount += x


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


def mainMenu():
    global startGame, tumbleAuto, playButtonHover, moveAbility, banMoveAbility, mouse_posx, mouse_posy, \
        settingsButtonHover
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
        musicLeftButtonHover, musicRightButtonHover

    masterVolumePercent = round(masterVolume * 100)
    musicVolumePercent = round(musicVolume * 100)
    masterVolume_text = font3.render((str(masterVolumePercent) + "%"), True, (255, 255, 255))
    musicVolume_text = font3.render((str(musicVolumePercent) + "%"), True, (255, 255, 255))
    masterVolumeBack_text = font3.render((str(masterVolumePercent) + "%"), True, (18, 15, 23))
    musicVolumeBack_text = font3.render((str(musicVolumePercent) + "%"), True, (18, 15, 23))

    screen.blit(asset_settings_menu, (0, 0))
    screen.blit(masterVolumeBack_text, (406, 191))
    screen.blit(masterVolume_text, (408, 190))
    screen.blit(musicVolumeBack_text, (394, 243))
    screen.blit(musicVolume_text, (396, 242))
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
    if (112 <= mouse_posx <= 140) and (187 <= mouse_posy <= 217) and masterLeftButtonClicked == False:
        screen.blit(asset_master_left_button_hover, (0, 0))
        masterLeftButtonHover = True
    # Click Button
    elif (112 <= mouse_posx <= 140) and (187 <= mouse_posy <= 217) and masterLeftButtonClicked == True:
        screen.blit(asset_master_left_button_clicked, (0, 0))
        masterLeftButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_master_left_button_normal, (0, 0))
        masterLeftButtonHover = False
    # Master Right -----------------------------------------------------------------------------------
    # Hover Button
    if (474 <= mouse_posx <= 504) and (187 <= mouse_posy <= 217) and masterRightButtonClicked == False:
        screen.blit(asset_master_right_button_hover, (0, 0))
        masterRightButtonHover = True
    # Click Button
    elif (474 <= mouse_posx <= 504) and (187 <= mouse_posy <= 217) and masterRightButtonClicked == True:
        screen.blit(asset_master_right_button_clicked, (0, 0))
        masterRightButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_master_right_button_normal, (0, 0))
        masterRightButtonHover = False
    # Music Left -----------------------------------------------------------------------------------
    # Hover Button
    if (112 <= mouse_posx <= 140) and (239 <= mouse_posy <= 270) and musicLeftButtonClicked == False:
        screen.blit(asset_music_left_button_hover, (0, 0))
        musicLeftButtonHover = True
    # Click Button
    elif (112 <= mouse_posx <= 140) and (239 <= mouse_posy <= 270) and musicLeftButtonClicked == True:
        screen.blit(asset_music_left_button_clicked, (0, 0))
        musicLeftButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_music_left_button_normal, (0, 0))
        musicLeftButtonHover = False
    # Music Right -----------------------------------------------------------------------------------
    # Hover Button
    if (474 <= mouse_posx <= 504) and (239 <= mouse_posy <= 270) and musicRightButtonClicked == False:
        screen.blit(asset_music_right_button_hover, (0, 0))
        musicRightButtonHover = True
    # Click Button
    elif (474 <= mouse_posx <= 504) and (239 <= mouse_posy <= 270) and musicRightButtonClicked == True:
        screen.blit(asset_music_right_button_clicked, (0, 0))
        musicRightButtonHover = False
    # Normal Button
    else:
        screen.blit(asset_music_right_button_normal, (0, 0))
        musicRightButtonHover = False
    # volume refresh
    step.set_volume(masterVolume)
    woodstep.set_volume(masterVolume)
    intro.set_volume(musicVolume)
    button.set_volume(masterVolume)
    griprevolver.set_volume(masterVolume)
    shot.set_volume(masterVolume)
    empty.set_volume(masterVolume)
    reload.set_volume(masterVolume)
    death.set_volume(masterVolume)
    playerhit.set_volume(masterVolume)
    banpain.set_volume(masterVolume)
    snipershot.set_volume(masterVolume)
    heartbeat.set_volume(masterVolume)
    breath.set_volume(masterVolume)
    intromusic.set_volume(musicVolume)
    door.set_volume(masterVolume)
    openbook.set_volume(masterVolume)
    turnpage.set_volume(masterVolume)
    cashregister.set_volume(masterVolume)
    error.set_volume(masterVolume)
    music.set_volume(musicVolume)
    potion.set_volume(masterVolume)
    sniper_reload.set_volume(masterVolume)


def playerHit(damage):
    global playerHP

    if playerHP > 0:
        playerHP -= damage
        playerHitSound_timer.start()


def playerDead():
    global dead, moveAbility, startGame
    dead = True
    # death screen
    screen.blit(asset_death_screen, (300 - 300, 300 - 300))
    screen.blit(deathScore_text, (278, 250))
    moveAbility = False
    startGame = False
    stopAllTimers(timerTuple)
    stopSounds()
    if playerHP == 0:
        death.stop()
        death.play()


def resetValues():
    global playerHP, moneyCount, revRoundsMag, revRoundsTotal, revolverFireRate, sniperRoundsMag, sniperRoundsTotal, \
        hpPotionCount, score, cloud1x, cloud2x, tumweed1x, store1x, store2x, cactusx, activeSlotx1, activeSlotx2, \
        bulletx, banHP, banx1, banFPx1, scopeWalk, ban2HP, banx2, ban2FPx1, scope2Walk, ban3HP, banx3, ban3FPx1, \
        scope3Walk, startGame, dead, moveAbility, banMoveAbility, interactText, buyText, sitting, standing, \
        insufFundsText, purchasedText, lookingLeft, lookingRight, hotbarSlot1, hotbarSlot2, hotbarSlot3, hotbarSlot4, \
        hotbarSlot5, hotbarSlot6, reloadUI, outAmmoUI, scopeScreen,ban1InScope,ban2InScope,ban3InScope,insideShop, \
        ownSniperRifle, catalog, catalogPage1, catalogPage2, catalogPage3, playerIdle, playerWalk, playerHolster, \
        playerLegsIdle, playerShoot, playerDrink, playerSniper, playerGrab, playButtonHover, playButtonClicked, \
        readyToFireRevolver, restartButtonHover, restartButtonClicked, mainMenuButtonHover, mainMenuButtonClicked, \
        resumeButtonHover, resumeButtonClicked, settingsButtonHover, settingsButtonClicked, mainMenu2ButtonHover, \
        mainMenu2ButtonClicked, confirmYesButtonHover, confirmYesButtonClicked, confirmNoButtonHover, \
        confirmNoButtonClicked, confirmationBox, settings, settingsDoneButtonHover, settingsDoneButtonClicked, \
        masterLeftButtonHover, masterLeftButtonClicked, masterRightButtonHover, masterRightButtonClicked, \
        musicLeftButtonHover, musicLeftButtonClicked, musicRightButtonHover, musicRightButtonClicked

    # player vals
    playerHP = 100
    moneyCount = 0
    revRoundsMag = 6
    revRoundsTotal = 24
    revolverFireRate = 120
    sniperRoundsMag = 1
    sniperRoundsTotal = 3
    hpPotionCount = 0
    score = 0

    # x-pos
    cloud1x = 100
    cloud2x = 600
    tumweed1x = 700
    store1x = 700
    store2x = 1400
    cactusx = 450
    activeSlotx1 = -50
    activeSlotx2 = -50
    bulletx = 330

    # ban 1
    banHP = 100
    banx1 = 1990
    banFPx1 = 300
    scopeWalk = 0
    # ban 2
    ban2HP = 100
    banx2 = 2490
    ban2FPx1 = 300
    scope2Walk = 0
    # ban 3
    ban3HP = 100
    banx3 = -1000
    ban3FPx1 = 300
    scope3Walk = 0

    moveAbility = True
    banMoveAbility = True
    interactText = False
    buyText = False
    sitting = False
    standing = True
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
    scopeScreen = False
    ban1InScope = False
    ban2InScope = False
    ban3InScope = False
    insideShop = False
    ownSniperRifle = True
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


def musicVolumeDown():
    global musicVolume
    if musicVolume > 0.1:
        musicVolume = musicVolume - 0.1


def musicVolumeUp():
    global musicVolume
    if musicVolume < 1:
        musicVolume = musicVolume + 0.1


def volumeButtonReset_timer_handler():
    global masterRightButtonClicked, musicRightButtonClicked, masterLeftButtonClicked, musicLeftButtonClicked
    masterLeftButtonClicked = False
    musicLeftButtonClicked = False
    masterRightButtonClicked = False
    musicRightButtonClicked = False


def revolver_reload_timer_handler():
    global revRoundsMag, revRoundsTotal
    if revRoundsTotal > 0:
        revRoundsTotal -= 1
        revRoundsMag += 1
    if revRoundsMag == 6:
        revolver_reload_timer.stop()


def sniper_reload_timer_handler():
    global sniperRoundsMag, sniperRoundsTotal
    if sniperRoundsTotal > 0:
        sniperRoundsTotal -= 1
        sniperRoundsMag += 1
    if sniperRoundsMag == 1:
        sniper_reload_timer.stop()


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


# timers (ms, timer_handler) (1000ms = 1sec)
revolver_reload_timer = simplegui.create_timer(revolverReloadSpeed, revolver_reload_timer_handler)
sniper_reload_timer = simplegui.create_timer(1000, sniper_reload_timer_handler)
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


# timers tuple
timerTuple = (revolver_reload_timer, sniper_reload_timer, music_timer, startGame_timer, revolverFireDelay_timer,
              drinkResetDelay_timer, resumeGame_timer, mainMenu_timer, playerHitSound_timer, confirmationBox_timer,
              volumeButtonReset_timer, settingsDone_timer, settingsMenu_timer)

# Main Menu Music
intromusic.play(-1)
resetValues()

# Game Loop (Screen Refresh Loop)
while True:
    # Event Handler ------------------------------------------------------------------------------------------
    for event in pygame.event.get():
        # When game is closed
        if event.type == pygame.QUIT:
            pygame.mixer.stop()
            music_timer.stop()
            stopAllTimers(timerTuple)
            pygame.quit()
            sys.exit()
        # Keyboard Handler
        if event.type == pygame.KEYDOWN:
            # Pause Game
            if event.key == pygame.K_ESCAPE and pause == False and startGame == True and dead == False:
                pygame.mixer.pause()
                screen.blit(asset_paused_darken, (0, 0))
                pause = True
            # Unpause Game
            elif event.key == pygame.K_ESCAPE and pause == True and settings == False:
                resumeGame_timer.start()
            # Exit settings
            elif event.key == pygame.K_ESCAPE and settings == True:
                settings = False
            if pause == False:
                # Walk left
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    walkLeft()
                # Walk right
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    walkRight()

                # Reloading
                if event.key == pygame.K_r:
                    # Revolver
                    if hotbarSlot1 == True:
                        if revRoundsMag < 6:
                            playerHolster = True
                            playerShoot = False
                            if revRoundsTotal > 0:
                                reload.stop()
                                reload.play()
                                reloadUI = False
                                revolver_reload_timer.start()
                    # Sniper Rifle
                    if hotbarSlot2 == True or scopeScreen == True:
                        if sniperRoundsMag < 1:
                            scopeScreen = False
                            playerSniper = True
                            if sniperRoundsTotal > 0:
                                sniper_reload.stop()
                                sniper_reload.play()
                                reloadUI = False
                                sniper_reload_timer.start()
                # Use Item (Space)
                if event.key == pygame.K_SPACE:
                    # Revolver fire
                    if hotbarSlot1 == True:
                        if moveAbility == True and readyToFireRevolver == True:
                            fire()
                            readyToFireRevolver = False
                            revolverFireDelay_timer.start()
                            if revRoundsMag <= 0:
                                reloadUI = True
                                outAmmoUI = False
                            if revRoundsTotal <= 0:
                                outAmmoUI = True
                                reloadUI = False
                    # Sniper Rifle fires
                    if hotbarSlot2 == True and ownSniperRifle == True and sniperRoundsMag >= 1:
                        fire()
                        if sniperRoundsMag <= 0:
                            reloadUI = True
                            outAmmoUI = False
                        if sniperRoundsTotal <= 0:
                            outAmmoUI = True
                            reloadUI = False
                    # HP Potion is used
                    if hotbarSlot6 == True and hpPotionCount > 0:
                        hpPotion()
                        drinkResetDelay_timer.start()
                        playerIdle = False
                # Aim Sniper Rifle
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if hotbarSlot2 == True and playerSniper == True and ownSniperRifle == True and insideShop == False:
                        scopeScreen = not scopeScreen
                        if scopeScreen == True:
                            breath.stop()
                            breath.play()
                            heartbeat.stop()
                            heartbeat.play()
                            ban1InScope = False
                            ban2InScope = False
                            ban3InScope = False
                # Switch to hotbar slot 1
                if event.key == pygame.K_1 and moveAbility == True and scopeScreen == False:
                    hotbarSlot1 = not hotbarSlot1
                    hotbarSlot2 = False
                    hotbarSlot3 = False
                    hotbarSlot4 = False
                    hotbarSlot5 = False
                    hotbarSlot6 = False
                    griprevolver.stop()
                    griprevolver.play()
                    interactText = False
                    playerHolster = not playerHolster
                    playerIdle = not playerIdle
                    playerSniper = False
                    if revRoundsMag <= 0 and revRoundsTotal > 0:
                        reloadUI = True
                    if hotbarSlot1 == False:
                        playerShoot = False
                        playerHolster = False
                # Switch to hotbar slot 2
                if event.key == pygame.K_2 and moveAbility == True:
                    hotbarSlot2 = not hotbarSlot2
                    hotbarSlot1 = False
                    hotbarSlot3 = False
                    hotbarSlot4 = False
                    hotbarSlot5 = False
                    hotbarSlot6 = False
                    playerHolster = False
                    playerShoot = False
                    if ownSniperRifle == True:
                        if sniperRoundsMag <= 0 and sniperRoundsTotal > 0:
                            reloadUI = True
                        playerSniper = not playerSniper
                        playerGrab = True
                        griprevolver.stop()
                        griprevolver.play()
                        playerIdle = False
                    if insideShop == True:
                        interactText = False
                # Switch to hotbar slot 3
                if event.key == pygame.K_3 and moveAbility == True and scopeScreen == False:
                    hotbarSlot3 = not hotbarSlot3
                    hotbarSlot1 = False
                    hotbarSlot2 = False
                    hotbarSlot4 = False
                    hotbarSlot5 = False
                    hotbarSlot6 = False
                    interactText = False
                    playerHolster = False
                    playerSniper = False
                # Switch to hotbar slot 4
                if event.key == pygame.K_4 and moveAbility == True and scopeScreen == False:
                    hotbarSlot4 = not hotbarSlot4
                    hotbarSlot1 = False
                    hotbarSlot2 = False
                    hotbarSlot3 = False
                    hotbarSlot5 = False
                    hotbarSlot6 = False
                    interactText = False
                    playerSniper = False
                    playerHolster = False
                # Switch to hotbar slot 5
                if event.key == pygame.K_5 and moveAbility == True and scopeScreen == False:
                    hotbarSlot5 = not hotbarSlot5
                    hotbarSlot1 = False
                    hotbarSlot2 = False
                    hotbarSlot3 = False
                    hotbarSlot4 = False
                    hotbarSlot6 = False
                    interactText = False
                    playerSniper = False
                    playerHolster = False
                # Switch to hotbar slot Q (6)
                if event.key == pygame.K_q and moveAbility == True and scopeScreen == False:
                    hotbarSlot6 = not hotbarSlot6
                    hotbarSlot1 = False
                    hotbarSlot2 = False
                    hotbarSlot3 = False
                    hotbarSlot4 = False
                    hotbarSlot5 = False
                    interactText = False
                    playerHolster = False
                    playerSniper = False
                    playerShoot = False
                # Enter Store
                if store1x <= 100 and store1x >= 0:
                    if playerShoot == False and scopeScreen == False and insideShop == False and playerSniper == False:
                        interactText = True
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            insideShop = True
                            lookingRight = True
                            lookingLeft = False
                            interactText = False
                            banMoveAbility = False
                            store1x = 150
                            store2x = 850
                            cactusx = -100
                            door.stop()
                            door.play()
                            banHP = -50
                            ban2HP = -50
                            ban3HP = -50
                # Exit Store
                if insideShop == True:
                    if (store1x - 200) >= 0:
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            insideShop = False
                            store1x = 50
                            store2x = 750
                            cactusx = -200
                            interactText = True
                            banMoveAbility = True
                            door.stop()
                            door.play()
                # Open Catalog
                if store1x + 420 <= 100 and store1x + 420 >= 0:
                    if playerHolster == False and playerShoot == False and insideShop == True and catalog == False\
                            and playerSniper == False:
                        interactText = True
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            catalog = not catalog
                            catalogPage1 = True
                            interactText = False
                            moveAbility = False
                            disableText()
                            openbook.stop()
                            openbook.play()
                    elif playerHolster == False and playerShoot == False and insideShop == True and catalog == True\
                            and playerSniper == False:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            catalog = False
                            catalogPage1 = False
                            catalogPage2 = False
                            catalogPage3 = False
                            disableText()
                            interactText = True
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
                            turnpage.stop()
                            turnpage.play()
                    elif catalogPage2 == True:
                        # Purchase Sniper Rifle
                        if event.key == pygame.K_2:
                            if moneyCount >= 1000 and ownSniperRifle == False:
                                purchasedText = True
                                ownSniperRifle = True
                                hotbarSlot2 = False
                                moneyCount -= 1000
                                cashregister.stop()
                                cashregister.play()
                            elif moneyCount < 1000 and ownSniperRifle == False:
                                insufFundsText = True
                                error.stop()
                                error.play()
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            catalogPage1 = False
                            catalogPage2 = False
                            catalogPage3 = True
                            disableText()
                            turnpage.stop()
                            turnpage.play()
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            catalogPage1 = True
                            catalogPage2 = False
                            catalogPage3 = False
                            disableText()
                            turnpage.stop()
                            turnpage.play()
                    elif catalogPage3 == True:
                        # Purchase Revolver Rounds
                        if event.key == pygame.K_1:
                            if moneyCount >= 50:
                                insufFundsText = False
                                purchasedText = True
                                revRoundsTotal += 24
                                moneyCount -= 50
                                cashregister.stop()
                                cashregister.play()
                            elif moneyCount < 50:
                                purchasedText = False
                                insufFundsText = True
                                error.stop()
                                error.play()
                        # Purchase Sniper Rifle Rounds
                        if event.key == pygame.K_2:
                            if moneyCount >= 100:
                                insufFundsText = False
                                purchasedText = True
                                sniperRoundsTotal += 6
                                moneyCount -= 100
                                cashregister.stop()
                                cashregister.play()
                            elif moneyCount < 100:
                                purchasedText = False
                                insufFundsText = True
                                error.stop()
                                error.play()
                        # Purchase HP Potion
                        if event.key == pygame.K_4:
                            if moneyCount >= 100:
                                insufFundsText = False
                                purchasedText = True
                                hpPotionCount += 1
                                moneyCount -= 100
                                cashregister.stop()
                                cashregister.play()
                            elif moneyCount < 100:
                                purchasedText = False
                                insufFundsText = True
                                error.stop()
                                error.play()
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            catalogPage1 = False
                            catalogPage2 = True
                            catalogPage3 = False
                            disableText()
                            turnpage.stop()
                            turnpage.play()
                # Shop Wall Collision
                if insideShop == True:
                    if (store1x + 700) <= 0:
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            moveAbility = False
                        elif event.key == pygame.K_a or event.key == pygame.K_RIGHT:
                            moveAbility = True
                            walkLeft()
        # Mouse Handler
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse Button 1
            if event.button == 1:
                # In Main Menu Screen
                # Play Button
                if startGame == False and settings == False and playButtonHover == True:
                    button.play()
                    intro.play()
                    startGame_timer.start()
                    playButtonHover = False
                    playButtonClicked = True
                if settings == False and settingsButtonHover == True:
                    button.play()
                    settingsMenu_timer.start()
                    settingsButtonHover = False
                    settingsButtonClicked = True

                # In Death Screen
                # Restart Game
                if startGame == False and dead == True and restartButtonHover == True:
                    button.play()
                    stopSounds()
                    intro.play()
                    startGame_timer.start()
                    restartButtonHover = False
                    restartButtonClicked = True
                    resetValues()
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


                # Use HP Beer
                if hotbarSlot6 == True and hpPotionCount > 0:
                    hpPotion()
                    drinkResetDelay_timer.start()
                    playerIdle = False
                # Fire Revolver
                if hotbarSlot1 == True:
                    if moveAbility == True and readyToFireRevolver == True:
                        fire()
                        readyToFireRevolver = False
                        revolverFireDelay_timer.start()
                # Fire Sniper Rifle
                if hotbarSlot2 == True and ownSniperRifle == True and sniperRoundsMag >= 1:
                    fire()
                    if sniperRoundsMag <= 0:
                        reloadUI = True
                        outAmmoUI = False
                        interactText = False
                    if sniperRoundsTotal <= 0:
                        outAmmoUI = True
                        reloadUI = False
                        interactText = False

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
        screen.blit(asset_sky_day, (300-300, 300-300))
        # ground
        screen.blit(asset_ground_sand, (0,403))
        # clouds
        screen.blit(asset_cloud1, (cloud1x-71, 75-37.5))
        screen.blit(asset_cloud2, (cloud2x-71, 175-54))
        # cactus
        screen.blit(asset_cactus, (cactusx+29-29,307-98))
        screen.blit(asset_cactus, (cactusx+789-29, 307-98))
        # store
        screen.blit(asset_store, (store1x+200-297, 212-198))
        # saloon
        screen.blit(asset_saloon, (store2x+200-294, 211-197.5))
        # tumbleweed
        screen.blit(asset_tumbleweed, (tumweed1x-38, 370-38.5))

        # bandit #1 alive
        if banHP > 0:
            # bandit 1 text
            screen.blit(ban1Tag, (banx1-30,232))
            screen.blit(ban1HPTag, (banx1-7,246))
            if ban1left == False:
                screen.blit(asset_bandit1, (banx1-39.5, 334-72))
            elif ban1left == True:
                screen.blit(asset_bandit1right, (banx1+32-39.5, 334-72))
        # bandit #2 alive
        if ban2HP > 0:
            screen.blit(ban2Tag, (banx2-30,225))
            screen.blit(ban2HPTag, (banx2-7,237))
            if ban2left == False:
                screen.blit(asset_bandit2, (banx2-40, 329-76.5))
            elif ban2left == True:
                screen.blit(asset_bandit2right, (banx2+24-40, 329-76.5))
        # bandit #3 alive
        if ban3HP > 0:
            screen.blit(ban3Tag, (banx3-32,231))
            screen.blit(ban3HPTag, (banx3-9,246))
            if ban3left == False:
                screen.blit(asset_bandit3, (banx3-40, 334-72))
            elif ban3left == True:
                screen.blit(asset_bandit3right, (banx3+30-40, 334-72))

        # shop interior
        if insideShop == True:
            screen.blit(asset_shop_interior, (store1x+550-800, 300-300))

        # character model
        if standing == True:
            if lookingRight == True:
                # drink potion right
                if playerDrink == True:
                    screen.blit(asset_player_drink_right, (254-50, 323-77))
                else:
                    # base player right
                    screen.blit(asset_player_right, (250-32.5, 329-75.5))
                # idle legs
                if playerLegsIdle == True:
                    screen.blit(asset_player_legs_idle_right, (250-32.5, 329-77))
                # sniper rifle on back
                if ownSniperRifle == True and playerSniper == False:
                    screen.blit(asset_sniper_rifle_right, (242-5, 341-39))
                # revolver on hip
                if playerShoot == False:
                    screen.blit(asset_revolver_vert_right, (246-9.5, 364-19.5))
                # holster
                screen.blit(asset_holster_right, (250-32.5, 335-75.5))
                # hp beer in hand right
                if hotbarSlot6 == True and hpPotionCount > 0 and playerIdle == True:
                    screen.blit(asset_hearty_beer_right, (245-14, 358-5))
                # holding sniper right
                if playerSniper == True and playerWalk == False:
                    screen.blit(asset_sniper_right, (260-53, 360-10.5))
                # idle arms
                if playerIdle == True:
                    screen.blit(asset_player_arms_idle, (249-32.5, 329-76))
                # hand on holster
                if playerHolster == True and playerWalk == False:
                    screen.blit(asset_player_holster_right, (250-32.5, 329-76))
                # grab sniper
                if playerGrab == True:
                    screen.blit(asset_player_holster_right, (250-32.5, 329-76))
                # walk right
                if playerWalk == True:
                    # drink walk
                    if playerDrink == True:
                        screen.blit(asset_player_legs_walk_right, (250-32.5, 329-77))
                    # hold sniper walk
                    elif playerSniper == True:
                        screen.blit(asset_sniper_right, (260-35, 360-10.5))
                        screen.blit(asset_player_legs_walk_right, (250-32.5, 329-77))
                        screen.blit(asset_player_arms_walk_right, (250-32.5, 329-76))
                    # holster walk
                    elif playerHolster == True:
                        screen.blit(asset_player_legs_walk_right, (250 - 32.5, 329 - 77))
                        if playerShoot == False:
                            screen.blit(asset_revolver_vert_right, (246 - 9.5, 364 - 19.5))
                        screen.blit(asset_holster_right, (250 - 32.5, 335 - 75.5))
                        screen.blit(asset_player_holsterwalk_right, (250-32.5, 329-76))

                    else:
                        # hp beer in hand right
                        if hotbarSlot6 == True and hpPotionCount > 0:
                            screen.blit(asset_hearty_beer_right, (263-14, 357-5))
                        # default walk
                        screen.blit(asset_player_arms_walk_right, (250-32.5, 329-76))
                        if ownSniperRifle == True and playerSniper == False:
                            screen.blit(asset_sniper_rifle_right, (242 - 5, 341 - 39))
                        screen.blit(asset_player_legs_walk_right, (250-32.5, 329-77))
                        if playerShoot == False:
                            screen.blit(asset_revolver_vert_right, (246 - 9.5, 364 - 19.5))
                        screen.blit(asset_holster_right, (250 - 32.5, 335 - 75.5))
                # bandana right
                screen.blit(asset_bandana_right, (250-32.5, 329-76))
                # extended arm right
                if playerShoot == True:
                    screen.blit(asset_revolver_right, (299-19.5, 321-9.5))
                    screen.blit(asset_player_shoot_right, (260-32.5, 329-77))
                    screen.blit(asset_muzzleflash_right, (bulletx-12, 313-5.5))

            if lookingLeft == True:
                # revolver on hip
                if playerShoot == False:
                    screen.blit(asset_revolver_vert_grip_left, (262 - 14, 346 - 4))
                # holding sniper left
                if playerSniper == True and playerWalk == False:
                    screen.blit(asset_sniper_left, (243-53, 360-10.5))
                # hp beer in hand right
                if hotbarSlot6 == True and hpPotionCount > 0 and playerIdle == True:
                    screen.blit(asset_hearty_beer_left, (254-14, 358-5))
                # drink potion left
                if playerDrink == True:
                    screen.blit(asset_player_drink_left, (249-50, 324-77))
                else:
                    # base player left
                    screen.blit(asset_player_left, (250-32.5, 329-75.5))
                # idle legs
                if playerLegsIdle == True:
                    screen.blit(asset_player_legs_idle_left, (250-32.5, 329-77))
                # idle arms
                if playerIdle == True:
                    screen.blit(asset_player_arms_idle, (250-32.5, 329-76))
                # hand on holster
                if playerHolster == True and playerWalk == False:
                    screen.blit(asset_player_holster_left, (250-32.5, 329-76))
                # grab sniper
                if playerGrab == True:
                    screen.blit(asset_player_holster_left, (250-32.5, 329-76))
                # sniper rifle on back
                if ownSniperRifle == True and playerSniper == False:
                    screen.blit(asset_sniper_rifle_left, (259-6, 341-39))
                    # walk left
                if playerWalk == True:
                    # drink walk
                    if playerDrink == True:
                        screen.blit(asset_player_legs_walk_left, (250-32.5, 329-77))
                    # hold sniper walk
                    elif playerSniper == True:
                        screen.blit(asset_sniper_left, (260-53, 359-10.5))
                        screen.blit(asset_player_left, (250 - 32.5, 329 - 75.5))
                        screen.blit(asset_player_arms_walk_left, (250-32.5, 329-76))
                        screen.blit(asset_player_legs_walk_left, (250-32.5, 329-77))
                    # holster walk
                    elif playerHolster == True:
                        screen.blit(asset_player_holsterwalk_left, (250-32.5, 329-76))
                        if ownSniperRifle == True and playerSniper == False:
                            screen.blit(asset_sniper_rifle_left, (259 - 6, 341 - 39))
                        screen.blit(asset_player_legs_walk_left, (250-32.5, 329-77))
                    else:
                        # hp beer in hand left
                        if hotbarSlot6 == True and hpPotionCount > 0:
                            screen.blit(asset_hearty_beer_left, (276-14, 357-5))
                        # default walk
                        screen.blit(asset_player_arms_walk_left, (250-32.5, 329-76))
                        if ownSniperRifle == True and playerSniper == False:
                            screen.blit(asset_sniper_rifle_left, (259 - 6, 341 - 39))
                        screen.blit(asset_player_legs_walk_left, (250 - 32.5, 329 - 77))
                # extended arm left
                if playerShoot == True:
                    screen.blit(asset_player_shoot_left, (240-32.5, 329-77))
                    screen.blit(asset_player_arms_idle, (250-32.5, 329-77))
                    screen.blit(asset_revolver_left, (202-19.5, 321-9.5))
                    screen.blit(asset_muzzleflash_left, (bulletx-250, 313-5.5))
                # bandana left
                screen.blit(asset_bandana_left, (250-32.5, 329-76))

        # catalog pages
        if insideShop == True:
            if catalog == True:
                if catalogPage1 == True:
                    screen.blit(asset_catalog_1, (300-300, 300-300))
                elif catalogPage2 == True:
                    screen.blit(asset_catalog_2, (300-300, 300-300))
                elif catalogPage3 == True:
                    screen.blit(asset_catalog_3, (300-300, 300-300))

        # catalog weapon prices
        if catalogPage2 == True:
            screen.blit(asset_text_owned, (245-24.5, 210-7))
            if ownSniperRifle == True:
                screen.blit(asset_text_owned, (245-24.5, 301-7))
            if ownSniperRifle == False:
                if moneyCount < 1000:
                    screen.blit(asset_text_1000_red, (248-21.5, 301-7.5))
                elif moneyCount >= 1000:
                    screen.blit(asset_text_1000_green, (248-21.5, 301-7.5))
        if catalogPage3 == True:
            if moneyCount < 100:
                # hearty beer
                screen.blit(asset_text_100_red, (527-21.5, 210-7.5))
                # 30-50 rounds
                screen.blit(asset_text_100_red, (257-21.5, 301-7.5))
            elif moneyCount >= 100:
                # hearty beer
                screen.blit(asset_text_100_green, (527-21.5, 210-7.5))
                # 30-50 rounds
                screen.blit(asset_text_100_green, (257-21.5, 301-7.5))
            if moneyCount < 50:
                # .45 rounds
                screen.blit(asset_text_50_red, (262-21.5, 208-7.5))
            elif moneyCount >= 50:
                # .45 rounds
                screen.blit(asset_text_50_green, (262-21.5, 208-7.5))

        if insideShop == False:
            # ban #1 dead
            if banHP <= 0:
                if ban1left == False:
                    screen.blit(asset_bandit1_dead, (banx1+50-73, 399-22))
                elif ban1left == True:
                    screen.blit(asset_bandit1right_dead, (banx1-50-73, 399-22))

            # ban #2 dead
            if ban2HP <= 0:
                if ban2left == False:
                    screen.blit(asset_bandit2_dead, (banx2+50-78.5, 399-22))
                elif ban2left == True:
                    screen.blit(asset_bandit2right_dead, (banx2-50-78.5, 399-22))

            # ban #3 dead
            if ban3HP <= 0:
                if ban3left == False:
                    screen.blit(asset_bandit3_dead, (banx3+50-73, 399-22.5))
                elif ban3left == True:
                    screen.blit(asset_bandit3right_dead, (banx3-50-73, 399-22.5))

        # ban 1 damage range
        if banHP > 0:
            if banx1 <= 290 and banx1 >= 210 and insideShop == False:
                playerHit(4)
        elif banHP == -50:
            banMove += 5
            banHP = 100
            banx1 = getBanditRespawn()

        # ban 2 damage range
        if ban2HP > 0:
            if banx2 <= 290 and banx2 >= 210 and insideShop == False:
                playerHit(4)
        elif ban2HP == -50:
            banMove += 5
            ban2HP = 100
            banx2 = getBanditRespawn()

        # ban 3 damage range
        if ban3HP > 0:
            if banx3 <= 290 and banx3 >= 210 and insideShop == False:
                playerHit(4)
        elif ban3HP == -50:
            banMove += 5
            ban3HP = 100
            banx3 = getBanditRespawn()

        # HUD
        if startGame == True:
            # hp
            screen.blit(asset_hp_icon, (25-12.5, 517-10))
            screen.blit(playerHP_text, (38, 505))
            # kills
            screen.blit(asset_kills_icon, (24-12.5, 540-10))
            screen.blit(playerScore_text, (40, 529))
            # money
            screen.blit(asset_money_icon, (24-12.5, 562-10))
            screen.blit(playerMoney_text, (40, 551))
            # ammo
            screen.blit(asset_ammo_icon, (25-12.5, 583-10))
            if hotbarSlot1 == True:
                screen.blit(revolverAmmo_text, (41, 571))
            elif hotbarSlot2 == True:
                screen.blit(sniperAmmo_text, (41, 571))
            else:
                screen.blit(blankAmmo_text, (41, 570))
            if reloadUI == True:
                if revRoundsMag <= 0 and hotbarSlot1 == True or sniperRoundsMag <= 0 and hotbarSlot2 == True:
                    screen.blit(reloadBack_text, (215.8, 233.8))
                    screen.blit(reloadFront_text, (215, 233))
            if outAmmoUI == True:
                if revRoundsTotal <= 0 and revRoundsMag <= 0 and hotbarSlot1 == True:
                    screen.blit(outAmmoBack_text, (215.8, 233.8))
                    screen.blit(outAmmoFront_text, (215, 233))
                if sniperRoundsTotal <= 0 and sniperRoundsMag <= 0 and hotbarSlot2 == True:
                    screen.blit(outAmmoBack_text, (215.8, 233.8))
                    screen.blit(outAmmoFront_text, (215, 233))
        # popup text
        if purchasedText == True:
            screen.blit(asset_text_purchased, (300-98.5, 70-9.5))
        if insufFundsText == True:
            screen.blit(asset_text_insufficient, (300-98.5, 70-9.5))
        #
        if moneyPick == True:
            showMoney = False

        if interactText == True:
            if sitting == True:
                screen.blit(interact_text, (218, 265))
            else:
                screen.blit(interact_text, (218, 235))

        if buyText == True:
            screen.blit(buy_text, (137, 255))

        # hotbar
        if startGame == True:
            screen.blit(asset_hotbar, (300-153.5, 560-28.5))
            screen.blit(asset_revolver, (300-153.5, 560-28.5))
            if ownSniperRifle == True:
                screen.blit(asset_sniper, (300-153.5, 560-28.5))
            if hpPotionCount > 0:
                screen.blit(asset_hearty_beer_icon, (500-153.5, 562-28.5))
                screen.blit(potionCount_text, (403, 537))

            screen.blit(asset_hotbar_select, (activeSlotx1-3, 565-33))

        # sniper scope
        if ownSniperRifle == True:
            if scopeScreen == True:
                # backdrop
                if lookingRight == True:
                    screen.blit(asset_scope_back_right, (300-300, 300-300))
                if lookingLeft == True:
                    screen.blit(asset_scope_back_left, (300-300, 300-300))

                # fp bandits
                if banx1 <= 600 and ban2InScope == False and ban3InScope == False:
                    if banx1 <= 600 and banx1 >= 250 and lookingRight == True or banx1 >= 0 and banx1 <= 250 and lookingLeft == True:
                        if banHP > 0:
                            ban1InScope = True
                            screen.blit(asset_bandit1_fp, (300-115, 350-180))

                if banx2 <= 600 and ban3InScope == False and ban1InScope == False:
                    if banx2 <= 600 and banx2 >= 250 and lookingRight == True or banx2 >= 0 and banx2 <= 250 and lookingLeft == True:
                        if ban2HP > 0:
                            ban2InScope = True
                            screen.blit(asset_bandit2_fp, (300-115, 350-180))

                if banx3 <= 600 and ban1InScope == False and ban2InScope == False:
                    if banx3 <= 600 and banx3 >= 250 and lookingRight == True or banx3 >= 0 and banx3 <= 250 and lookingLeft == True:
                        if ban3HP > 0:
                            ban3InScope = True
                            screen.blit(asset_bandit3_fp, (300-115, 350-180))

                            # scope
                screen.blit(asset_sniperscope, (300-300, 300-300))
                if hotbarSlot2 == True:
                    screen.blit(asset_ammo_icon, (25-12.5, 583-10))
                    screen.blit(sniperAmmo_text, (41, 571))
            else:
                breath.stop()
                heartbeat.stop()

        if banMoveAbility == True:
            banMove = 8
        elif banMoveAbility == False:
            banMove = 0



        # Constant Refresh -------------------------------------------------------------------------------------

        # Player Model Refresh
        playerLegsIdle = True
        playerWalk = False

        playerGrab = False
        if playerHolster == False and playerShoot == False and playerDrink == False:
            playerIdle = True
        if playerSniper == True and sniperRoundsMag > 0 and insideShop == False:
            interactText = True
        if (playerHolster == True or playerSniper == True) and insideShop == True:
            screen.blit(shopWarning_text, (store1x + 527, 207))

        # Check if dead
        if playerHP <= 0:
            playerDead()

        # text refresh
        ban1HPTag = font1.render(("HP: " + str(banHP)), True, (255, 255, 255))
        ban2HPTag = font1.render(("HP: " + str(ban2HP)), True, (255, 255, 255))
        ban3HPTag = font1.render(("HP: " + str(ban3HP)), True, (255, 255, 255))
        playerHP_text = font2.render((str(playerHP)), True, (255, 255, 255))
        playerScore_text = font2.render((str(score)), True, (255, 255, 255))
        playerMoney_text = font2.render((str(moneyCount)), True, (255, 255, 255))
        revolverAmmo_text = font2.render((str(revRoundsMag) + "/" + str(revRoundsTotal)), True, (255, 255, 255))
        sniperAmmo_text = font2.render((str(sniperRoundsMag) + "/" + str(sniperRoundsTotal)), True, (255, 255, 255))
        potionCount_text = font1.render((str(hpPotionCount)), True, (255, 255, 255))
        deathScore_text = font1.render(("Score: " + str(score)), True, (255, 255, 255))
        masterVolume_text = font1.render((str(masterVolume)), True, (255, 255, 255))
        musicVolume_text = font1.render((str(musicVolume)), True, (255, 255, 255))

        # volume refresh
        step.set_volume(masterVolume)
        woodstep.set_volume(masterVolume)
        intro.set_volume(musicVolume)
        button.set_volume(masterVolume)
        griprevolver.set_volume(masterVolume)
        shot.set_volume(masterVolume)
        empty.set_volume(masterVolume)
        reload.set_volume(masterVolume)
        death.set_volume(masterVolume)
        playerhit.set_volume(masterVolume)
        banpain.set_volume(masterVolume)
        snipershot.set_volume(masterVolume)
        heartbeat.set_volume(masterVolume)
        breath.set_volume(masterVolume)
        intromusic.set_volume(musicVolume)
        door.set_volume(masterVolume)
        openbook.set_volume(masterVolume)
        turnpage.set_volume(masterVolume)
        cashregister.set_volume(masterVolume)
        error.set_volume(masterVolume)
        music.set_volume(musicVolume)
        potion.set_volume(masterVolume)
        sniper_reload.set_volume(masterVolume)

        # building loop
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

        # cloud pos
        cloud1x -= cloudAuto
        if cloud1x + 85 <= -100:
            cloud1x = 800
        cloud2x -= cloudAuto
        if cloud2x + 85 <= -100:
            cloud2x = 1100

        # tumweed pos
        tumweed1x -= tumbleAuto
        if tumweed1x <= - 2000:
            tumweed1x = 1100

        # bullet reset
        bulletx = -330

        # ban 1 position
        if banHP > 0:
            if banx1 <= 600:
                scopeWalk += 6
            if banx1 >= 600 or banx1 <= 0:
                scopeWalk = 5
            if banx1 >= 280:
                banx1 -= banMove
                ban1left = False
            if banx1 <= 220:
                banx1 += banMove
                ban1left = True
        elif banHP <= 0:
            banHP -= 1
            # ban 2 position
        if ban2HP > 0:
            if banx2 <= 600:
                scope2Walk += 6
            if banx2 >= 600 or banx2 <= 0:
                scope2Walk = 5
            if banx2 >= 280:
                banx2 -= banMove
                ban2left = False
            if banx2 <= 220:
                banx2 += banMove
                ban2left = True
        elif ban2HP <= 0:
            ban2HP -= 1
        # ban 3 position
        if ban3HP > 0:
            if banx3 <= 600:
                scope3Walk += 6
            if banx3 >= 600 or banx3 <= 0:
                scope3Walk = 5
            if banx3 >= 280:
                banx3 -= banMove
                ban3left = False
            if banx3 <= 220:
                banx3 += banMove
                ban3left = True
        elif ban3HP <= 0:
            ban3HP -= 1



    pygame.display.update()
    clock.tick(25)

# End
