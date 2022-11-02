from flask import Flask

# 어플리케이션 팩토리
def create_app(config=None):

    app = Flask(__name__)
    
    # 여기에서 주어진 config 에 따라 추가 설정을 합니다.
    if config is not None:
        app.config.update(config)
    
    from flask_kbo.views.main_views import main_bp
    from flask_kbo.views.res_views import res_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(res_bp, url_prefix='/res')

    return app

if __name__ == "__main__":
  app = create_app()
  app.run()