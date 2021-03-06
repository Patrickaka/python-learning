import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
import game_fuctions


def run_game():

    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    game_fuctions.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        game_fuctions.check_events(ai_settings, screen, stats, play_button,
                                   ship, bullets)
        if stats.game_active:
            ship.update()
            game_fuctions.update_bullets(ai_settings, screen, ship, aliens,
                                         bullets)
            game_fuctions.update_aliens(ai_settings, stats, screen, ship,
                                        aliens, bullets)

        game_fuctions.update_screen(ai_settings, screen, stats, ship, aliens,
                                    bullets, play_button)
*/-***

run_game()
