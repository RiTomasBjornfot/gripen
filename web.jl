using Dash, DashHtmlComponents, DashCoreComponents, PlotlyBase
using Pipe, DelimitedFiles

read_data(fname) = @pipe (read(fname, String)
	|> split(_, "\n")
	|> [parse.(Float64, split(x, " ")) for x∈_[1:end-1]]
	|> Iterators.flatten
	|> collect
)

app = dash()

# some data
#fname = "data/gamla_acc_gamla_ble"
#fname = "data/nya_acc_gamla_ble"
fname = "data/u1"

# layout
app.layout = html_div() do
	html_h1("Data from BLE unit"),
	dcc_graph(
		id = "plot",
		figure = @pipe (readdlm(fname)
			#|> _[:, 1:end-9]
			|> reshape(_', length(_))
			|> [_[1:3:end] _[2:3:end] _[3:3:end]] 
			|> Plot
		)
	)
end

run_server(app, "0.0.0.0")
