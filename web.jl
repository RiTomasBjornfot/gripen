using Dash, DashHtmlComponents, DashCoreComponents, PlotlyBase
using Pipe
read_data(fname) = @pipe (read(fname, String)
	|> split(_, "\n")
	|> [parse.(Float64, split(x, " ")) for x∈_[1:end-1]]
	|> Iterators.flatten
	|> collect
)

app = dash()

# some data
fname = "data/1623910259"

# layout
app.layout = html_div() do
	html_h1("Data from BLE unit"),
	dcc_graph(
		id = "plot",
		figure = read_data(fname) |> Plot
	),
end

run_server(app, "0.0.0.0")
