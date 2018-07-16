require 'json'

#Eye.config do
#  logger '/home/vagrant/eye.log'
#end

WORKING_DIR = File.expand_path(__dir__)

%w[dev stage prod].each do |environment|
   Eye.application "#{environment}" do
     working_dir WORKING_DIR

     jobs = JSON.load(File.read("#{WORKING_DIR}/#{environment}.json"))
     jobs.each do |name, command|
       process "#{name}" do
         pid_file "#{WORKING_DIR}/#{name}-#{environment}.pid"
         start_command "#{command}"
         daemonize false
         stdall "#{WORKING_DIR}/eye.log"
         stop_signals [:INT, 30.seconds, :TERM, 10.seconds, :KILL]
       end
     end
   end
end
