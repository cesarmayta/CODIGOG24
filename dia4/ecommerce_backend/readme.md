#paso 1
npm init -y

#paso 2
npm install express mysql2 dotenv

#paso 3
npm install --save-dev nodemon

#paso 4
scripts
"start": "node src/index.js",
"dev": "nodemon src/index.js",