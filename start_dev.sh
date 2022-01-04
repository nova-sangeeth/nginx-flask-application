# start_dev
echo "Starting to build and deploy the application."
docker-compose down && docker-compose build && docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d && docker-compose ps
echo "Done..."