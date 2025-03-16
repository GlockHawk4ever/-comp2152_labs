using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;

public class ProjectSummaryViewComponent : ViewComponent
{
    public IViewComponentResult Invoke()
    {
        return View();
    }
}
