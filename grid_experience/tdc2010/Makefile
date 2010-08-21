root_dir=.
browser="firefox"
pattern="*"

selenium_up:
	@echo "===================="
	@echo "Starting selenium..."
	@echo "===================="
	@java -jar ${root_dir}/lib/selenium-server.jar 2> /dev/null > /dev/null &
	@echo "Started."

selenium_down:
	@echo "==================="
	@echo "Killing selenium..."
	@echo "==================="
	@-ps aux | egrep selenium | egrep -v egrep | awk '{ print $$2 }' | xargs kill -9
	@echo "Killed."

wait:
	@echo "=========="
	@echo "Waiting..."
	@echo "=========="
	@sleep 10

acceptance:
	@make selenium_up
	@make wait
	@echo "================="
	@echo "Starting tests..."
	@echo "================="

	@pyccuracy-console -d ${root_dir}/tests/acceptance/ -p "${pattern}.acc" -l pt-br -v 3 -b ${browser} -u http://localhost:8000

grid_acceptance:
	@echo "=========================="
	@echo "Starting parallel tests..."
	@echo "=========================="

	@pyccuracy-console -d ${root_dir}/tests/acceptance/ -p "${pattern}.acc" -l pt-br -v 1 -b ${browser} -u http://localhost:8000 -w 6
