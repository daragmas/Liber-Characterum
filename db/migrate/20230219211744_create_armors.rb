class CreateArmors < ActiveRecord::Migration[7.0]
  def change
    create_table :armors do |t|
      t.string :name
      t.string :coverage
      t.integer :ap
      t.float :wt
      t.string :availability
      t.string :book
      t.string :special
      t.string :alignment

      t.timestamps
    end
  end
end
