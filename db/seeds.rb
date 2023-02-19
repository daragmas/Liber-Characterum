# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the bin/rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: "Star Wars" }, { name: "Lord of the Rings" }])
#   Character.create(name: "Luke", movie: movies.first)

require 'csv'

puts 'Starting Seed'

puts "Seeding Traits"

csv_text = File.read('db/database_csvs/traits.csv')
csv = CSV.parse(csv_text, :headers =>true, :encoding => 'ISO-8859-1')

csv.each do |row|
    t = Trait.create!(name: row["Name"], description: row["Description"])
end