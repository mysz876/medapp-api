from flask import Flask

def load_blueprint(app: Flask):
    from application.routes.branch_route import branch_bp
    app.register_blueprint(branch_bp, url_prefix='/branch')

    from application.routes.specialization_route import specialization_bp
    app.register_blueprint(specialization_bp, url_prefix='/specialization')

    from application.routes.doctor_route import doctor_bp
    app.register_blueprint(doctor_bp, url_prefix='/doctor')
