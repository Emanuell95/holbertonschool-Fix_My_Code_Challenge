###
#
#  Sort integer arguments (ascending) 
#
###

result = []
ARGV.each do |arg|
  # skip if not integer
  next unless arg =~ /^-?\d+$/

  # convert to integer
  i_arg = arg.to_i

  # insert in sorted order
  inserted = false
  result.each_with_index do |val, index|
    if i_arg < val
      result.insert(index, i_arg)
      inserted = true
      break
    end
  end

  # if not inserted, append to the end
  result << i_arg unless inserted
end

puts result