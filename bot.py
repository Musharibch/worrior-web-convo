<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝐖𝐎𝐑𝐑𝐈𝐎𝐑 𝐂𝐎𝐍𝐕𝐎 𝐒𝐄𝐑𝐕𝐄𝐑 - Access Portal</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }
        
        body::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255, 255, 255, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(120, 119, 198, 0.2) 0%, transparent 50%);
            animation: backgroundFloat 8s ease-in-out infinite;
        }
        
        @keyframes backgroundFloat {
            0%, 100% { transform: scale(1) rotate(0deg); }
            50% { transform: scale(1.1) rotate(2deg); }
        }
        
        .auth-container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(25px);
            border-radius: 30px;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.2), 
                        0 0 0 1px rgba(255, 255, 255, 0.3);
            max-width: 480px;
            width: 100%;
            overflow: hidden;
            position: relative;
            z-index: 1;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .auth-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
            border-radius: 30px;
            z-index: -1;
        }
        
        .auth-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 50px 30px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .auth-header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: headerGlow 4s ease-in-out infinite;
        }
        
        @keyframes headerGlow {
            0%, 100% { transform: scale(1) rotate(0deg); }
            50% { transform: scale(1.2) rotate(180deg); }
        }
        
        .auth-title {
            font-size: 3rem;
            font-weight: 900;
            margin-bottom: 15px;
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
            position: relative;
            z-index: 1;
            letter-spacing: -2px;
        }
        
        .auth-subtitle {
            font-size: 1.1rem;
            opacity: 0.95;
            position: relative;
            z-index: 1;
            font-weight: 500;
        }
        
        .auth-tabs {
            display: flex;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-bottom: 1px solid #dee2e6;
        }
        
        .auth-tab {
            flex: 1;
            padding: 25px 20px;
            text-align: center;
            cursor: pointer;
            font-weight: 700;
            color: #6c757d;
            transition: all 0.4s ease;
            position: relative;
            background: transparent;
            border: none;
            font-size: 16px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .auth-tab::before {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            width: 0;
            height: 4px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            transition: all 0.4s ease;
            transform: translateX(-50%);
        }
        
        .auth-tab:hover {
            background: linear-gradient(135deg, #e9ecef 0%, #f8f9fa 100%);
            color: #667eea;
            transform: translateY(-2px);
        }
        
        .auth-tab.active {
            color: #667eea;
            background: white;
            box-shadow: 0 -5px 15px rgba(102, 126, 234, 0.1);
        }
        
        .auth-tab.active::before {
            width: 80%;
        }
        
        .auth-form {
            display: none;
            padding: 45px 35px;
        }
        
        .auth-form.active {
            display: block;
            animation: fadeInUp 0.5s ease;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .form-group {
            margin-bottom: 30px;
            position: relative;
        }
        
        .form-group i {
            position: absolute;
            left: 18px;
            top: 50%;
            transform: translateY(-50%);
            color: #6c757d;
            font-size: 18px;
            z-index: 2;
            transition: all 0.3s ease;
        }
        
        label {
            display: block;
            margin-bottom: 10px;
            font-weight: 700;
            color: #495057;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 20px 20px 20px 55px;
            border: 2px solid #e9ecef;
            border-radius: 15px;
            font-size: 16px;
            transition: all 0.4s ease;
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            font-family: inherit;
            font-weight: 500;
        }
        
        input[type="text"]:focus,
        input[type="password"]:focus {
            outline: none;
            border-color: #667eea;
            background: white;
            box-shadow: 0 0 0 6px rgba(102, 126, 234, 0.1);
            transform: translateY(-2px);
        }
        
        input[type="text"]:focus + i,
        input[type="password"]:focus + i {
            color: #667eea;
            transform: translateY(-50%) scale(1.1);
        }
        
        .btn {
            width: 100%;
            padding: 20px;
            border: none;
            border-radius: 15px;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.4s ease;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            position: relative;
            overflow: hidden;
        }
        
        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.6s;
        }
        
        .btn:hover::before {
            left: 100%;
        }
        
        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }
        
        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 20px 40px rgba(102, 126, 234, 0.4);
        }
        
        .btn-success {
            background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
            color: white;
            box-shadow: 0 10px 20px rgba(40, 167, 69, 0.3);
        }
        
        .btn-success:hover {
            transform: translateY(-3px);
            box-shadow: 0 20px 40px rgba(40, 167, 69, 0.4);
        }
        
        .btn-warning {
            background: linear-gradient(135deg, #ffc107 0%, #fd7e14 100%);
            color: #212529;
            box-shadow: 0 10px 20px rgba(255, 193, 7, 0.3);
        }
        
        .btn-warning:hover {
            transform: translateY(-3px);
            box-shadow: 0 20px 40px rgba(255, 193, 7, 0.4);
        }
        
        .alert {
            padding: 18px 25px;
            border-radius: 12px;
            margin-top: 25px;
            font-weight: 600;
            text-align: center;
            border: 2px solid;
            animation: slideIn 0.5s ease;
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        .alert-danger {
            background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
            color: #721c24;
            border-color: #f5c6cb;
        }
        
        .alert-success {
            background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
            color: #155724;
            border-color: #c3e6cb;
        }
        
        .form-footer {
            text-align: center;
            margin-top: 35px;
            padding-top: 25px;
            border-top: 2px solid #e9ecef;
            color: #6c757d;
            font-size: 14px;
            font-weight: 500;
        }
        
        .floating-elements {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: -1;
        }
        
        .floating-element {
            position: absolute;
            opacity: 0.1;
            animation: floatAround 15s infinite linear;
            font-size: 2rem;
            color: white;
        }
        
        .floating-element:nth-child(1) {
            top: 10%;
            left: 10%;
            animation-delay: 0s;
        }
        
        .floating-element:nth-child(2) {
            top: 70%;
            left: 80%;
            animation-delay: 5s;
        }
        
        .floating-element:nth-child(3) {
            top: 50%;
            left: 20%;
            animation-delay: 10s;
        }
        
        @keyframes floatAround {
            0% { transform: translateY(0px) rotate(0deg); }
            25% { transform: translateY(-50px) rotate(90deg); }
            50% { transform: translateY(-100px) rotate(180deg); }
            75% { transform: translateY(-50px) rotate(270deg); }
            100% { transform: translateY(0px) rotate(360deg); }
        }
        
        @media (max-width: 480px) {
            .auth-container {
                margin: 10px;
                border-radius: 25px;
            }
            
            .auth-header {
                padding: 35px 25px;
            }
            
            .auth-title {
                font-size: 2.5rem;
            }
            
            .auth-form {
                padding: 35px 25px;
            }
            
            .auth-tab {
                padding: 20px 15px;
                font-size: 14px;
            }
        }
    </style>
</head>
<body>
    <div class="floating-elements">
        <div class="floating-element"><i class="fas fa-star"></i></div>
        <div class="floating-element"><i class="fas fa-gem"></i></div>
        <div class="floating-element"><i class="fas fa-crown"></i></div>
    </div>
    
    <div class="auth-container">
        <div class="auth-header">
            <h1 class="auth-title">𝐌𝐑 𝐖𝐎𝐑𝐑𝐈𝐎𝐑</h1>
            <p class="auth-subtitle">Welcome To 𝐖𝐎𝐑𝐑𝐈𝐎𝐑 𝐂𝐎𝐍𝐕𝐎 𝐒𝐄𝐑𝐕𝐄𝐑</p>
        </div>
        
        <div class="auth-tabs">
            <button class="auth-tab active" onclick="switchAuthTab('login')">
                <i class="fas fa-sign-in-alt"></i> Login
            </button>
            <button class="auth-tab" onclick="switchAuthTab('register')">
                <i class="fas fa-user-plus"></i> Register
            </button>
            <button class="auth-tab" onclick="switchAuthTab('admin')">
                <i class="fas fa-user-shield"></i> Admin Login
            </button>
        </div>
        
        <div id="login-form" class="auth-form active">
            <form action="/login" method="post">
                <div class="form-group">
                    <label for="login-username">
                        <i class="fas fa-user"></i> Username
                    </label>
                    <input type="text" id="login-username" name="username" placeholder="Enter your username" required>
                    <i class="fas fa-user"></i>
                </div>
                <div class="form-group">
                    <label for="login-password">
                        <i class="fas fa-lock"></i> Password
                    </label>
                    <input type="password" id="login-password" name="password" placeholder="Enter your password" required>
                    <i class="fas fa-lock"></i>
                </div>
                <button type="submit" class="btn btn-primary">
                    <i class="fas fa-sign-in-alt"></i> Access Platform
                </button>
            </form>
            
            
                
            
            
            <div class="form-footer">
                <i class="fas fa-shield-alt"></i> Secure authentication powered by advanced encryption
            </div>
        </div>
        
        <div id="register-form" class="auth-form">
            <form action="/register" method="post">
                <div class="form-group">
                    <label for="register-username">
                        <i class="fas fa-user"></i> Username
                    </label>
                    <input type="text" id="register-username" name="username" placeholder="Enter your username" required>
                    <i class="fas fa-user"></i>
                </div>
                <div class="form-group">
                    <label for="register-password">
                        <i class="fas fa-lock"></i> Password
                    </label>
                    <input type="password" id="register-password" name="password" placeholder="Create a password" required>
                    <i class="fas fa-lock"></i>
                </div>
                <div class="form-group">
                    <label for="confirm-password">
                        <i class="fas fa-lock"></i> Confirm Password
                    </label>
                    <input type="password" id="confirm-password" name="confirm_password" placeholder="Confirm your password" required>
                    <i class="fas fa-lock"></i>
                </div>
                <button type="submit" class="btn btn-success">
                    <i class="fas fa-user-plus"></i> Create Account
                </button>
            </form>
            
            
                
            
            
            <div class="form-footer">
                <i class="fas fa-info-circle"></i> New accounts require administrator approval
            </div>
        </div>
        
        <div id="admin-form" class="auth-form">
            <form action="/admin_login" method="post">
                <div class="form-group">
                    <label for="admin-username">
                        <i class="fas fa-user-shield"></i> Admin Username
                    </label>
                    <input type="text" id="admin-username" name="username" placeholder="Enter admin username" required>
                    <i class="fas fa-user-shield"></i>
                </div>
                <div class="form-group">
                    <label for="admin-password">
                        <i class="fas fa-key"></i> Admin Password
                    </label>
                    <input type="password" id="admin-password" name="password" placeholder="Enter admin password" required>
                    <i class="fas fa-key"></i>
                </div>
                <button type="submit" class="btn btn-warning">
                    <i class="fas fa-user-shield"></i> Admin Access
                </button>
            </form>
            
            
                
            
            
            <div class="form-footer">
                <i class="fas fa-shield-alt"></i> Administrator access with elevated privileges
            </div>
        </div>
    </div>

    <script>
        function switchAuthTab(tab) {
            // Remove active class from all tabs and forms
            document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.auth-form').forEach(f => f.classList.remove('active'));
            
            // Add active class to selected tab and form
            if (tab === 'login') {
                document.querySelector('.auth-tab:first-child').classList.add('active');
                document.getElementById('login-form').classList.add('active');
            } else if (tab === 'register') {
                document.querySelector('.auth-tab:nth-child(2)').classList.add('active');
                document.getElementById('register-form').classList.add('active');
            } else if (tab === 'admin') {
                document.querySelector('.auth-tab:nth-child(3)').classList.add('active');
                document.getElementById('admin-form').classList.add('active');
            }
        }
        
        // Add interactive effects
        document.addEventListener('DOMContentLoaded', function() {
            const inputs = document.querySelectorAll('input');
            inputs.forEach(input => {
                input.addEventListener('focus', function() {
                    this.parentElement.style.transform = 'scale(1.02)';
                    this.parentElement.style.transition = 'transform 0.3s ease';
                });
                
                input.addEventListener('blur', function() {
                    this.parentElement.style.transform = 'scale(1)';
                });
            });
            
            // Add typing effect to title
            const title = document.querySelector('.auth-title');
            const text = title.textContent;
            title.textContent = '';
            let i = 0;
            const typeWriter = () => {
                if (i < text.length) {
                    title.textContent += text.charAt(i);
                    i++;
                    setTimeout(typeWriter, 100);
                }
            };
            setTimeout(typeWriter, 500);
        });
    </script>
</body>
</html>
