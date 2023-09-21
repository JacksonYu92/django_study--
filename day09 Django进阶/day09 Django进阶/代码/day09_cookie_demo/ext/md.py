from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):

        # 如果是登录的界面，直接向后运行
        if request.path_info == "/login/":
            return

        # 除了/login/以外的其他的页面，都需要做验证
        info_dict = request.session.get('info')
        if info_dict:
            # 给request中赋值
            request.info_dict = info_dict
            return
        return redirect('/login/')
