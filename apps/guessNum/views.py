from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from apps.guessNum.models import GameNumberModel
from apps.users.models import User, Player, PlayerGuessNums


class IndexVIew(View):
    def get(self, request):
        return render(request, 'guessNumHtmls/guessIndex.html')


# 创建游戏
class CreateNewGameView(View):
    def post(self, request):
        num = request.POST.get('num')
        playerList = request.POST.get('playerList')
        playerList = list(set(playerList))
        GameNumber = GameNumberModel.objects.create(num=num)
        GameNumber.save()
        for playerId in playerList:
            Player.objects.create(user_id=playerId, game_id=GameNumber.id)
        content = {
            'success': True,
            'message': '游戏创建成功'
        }
        return JsonResponse(content)


class StartGuessView(View):
    def get(self, request):
        playerId = request.GET.get('playerId')
        guessNum = request.GET.get('guessNum')
        game = Player.objects.get(id=playerId).game
        if game.status == 2:
            content = {
                'success': False,
                'message': '该游戏已结束'
            }
            return JsonResponse(content)
        PlayerGuessNums.objects.create(player_id=playerId, num=guessNum)
        content = {
            'success': True,
            'message': '猜测成功'
        }
        if guessNum == game.num:
            game.status = 2
            game.winner_id = playerId
            game.save()
            content = {
                'success': True,
                'message': '恭喜你答对了'
            }
            return JsonResponse(content)
        return JsonResponse(content)




