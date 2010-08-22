root_dir=.
browser="firefox"
pattern="*"
number_of_workers=1
port=5555

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

kill_workers:
	@echo "Killing workers from port $(begin) to $(end)..."
	@kill `lsof -t -i :$(begin)-$(end)`
	@echo "Killed."

hub:
	@echo "Launching Selenium Grid..."
	@ant -f lib/selenium-grid-1.0.8/build.xml launch-hub 2> /dev/null > /dev/null &
	@echo "Grid launched."

run_worker:
	@ant -f lib/selenium-grid-1.0.8/build.xml -Dport $(port) -Denvironment *$(browser) launch-remote-control 2> /dev/null > /dev/null &

workers:
	@for ((a=$(port); a<($(port)+$(number_of_workers)); a++)) do echo "Launching worker (port=$$a, browser=$(browser))..." && make run_worker port=$$a; done

acceptance:
	#@make selenium_up
	#@make wait
	@echo "================="
	@echo "Starting tests..."
	@echo "================="

	@pyccuracy-console -d ${root_dir}/tests/acceptance/ -p "${pattern}.acc" -l pt-br -v 3 -b ${browser} -u http://localhost:8000

grid_acceptance:
	@echo "=========================="
	@echo "Starting parallel tests..."
	@echo "=========================="

	@pyccuracy-console -d ${root_dir}/tests/acceptance/ -p "${pattern}.acc" -l pt-br -v 1 -b ${browser} -u http://localhost:8000 -w 6
