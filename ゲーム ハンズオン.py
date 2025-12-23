import pygame

#画面サイズを定義
W, H = 320, 270
#タイル数
TILE_X = 16
TILE_Y = 14



def main():
    """メイン関数
    """
    #pygameの初期化
    pygame.init()
    #画面を作成
    win = pygame.display.set_mode((W, H))
    #クロックを作成
    clock = pygame.time.Clock()

    #イベントループ
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

        #背景を塗りつぶす
        win.fill((135, 206, 235))

        #画面を更新
        pygame.display.flip()

        #フレームレートを設定
        clock.tick(30)

if __name__ == "__main__":
    main()