import __init__ as init

print('이름과 직업을 입력해 주십시오')
print('1. 전사  2. 궁수  3. 마법사')
print('ex) player1 1')
print('    player2 2')
name, job = input().split()

player = init.player(name,job)

print('스테이터스')
player.get_status()
print()
print('스킬 사용')
player.using_skill()